#!/usr/bin/env bash

# 
# simple whiptail TUI to check/set the current CPU Governor for a proxmox node.
#

set -euo pipefail

# Ensure script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Error: Please run this script as root." >&2
    exit 1
fi

SYS_CPU_DIR="/sys/devices/system/cpu"
AVAIL_GOV_FILE="$SYS_CPU_DIR/cpu0/cpufreq/scaling_available_governors"
CURR_GOV_FILE="$SYS_CPU_DIR/cpu0/cpufreq/scaling_governor"
SERVICE_PATH="/etc/systemd/system/set-cpu-governor.service"

# Check if cpufreq interface exists
if [ ! -f "$AVAIL_GOV_FILE" ]; then
    whiptail --title "Error" --msgbox "CPU frequency scaling interface not found.\nCheck if pstate/cpufreq drivers are enabled on this host." 10 60
    exit 1
fi

# Fetch available and current governors
AVAILABLE_GOVERNORS=$(cat "$AVAIL_GOV_FILE")
CURRENT_GOVERNOR=$(cat "$CURR_GOV_FILE")

# Prepare whiptail menu items with explicit indicators
MENU_OPTIONS=()
for gov in $AVAILABLE_GOVERNORS; do
    if [ "$gov" == "$CURRENT_GOVERNOR" ]; then
        desc="<-- ACTIVE GOVERNOR"
    else
        desc="Profile option"
    fi
    MENU_OPTIONS+=("$gov" "$desc")
done

# Show governor selection menu
SELECTED_GOVERNOR=$(whiptail --title "Proxmox CPU Governor Manager" \
    --menu "Active Governor: [$CURRENT_GOVERNOR]\nSelect a new scaling governor:" \
    15 65 6 "${MENU_OPTIONS[@]}" 3>&1 1>&2 2>&3)

# Handle cancel/escape
if [ -z "$SELECTED_GOVERNOR" ]; then
    echo "No changes made."
    exit 0
fi

# Apply the governor immediately across all cores
echo "$SELECTED_GOVERNOR" | tee $SYS_CPU_DIR/cpu*/cpufreq/scaling_governor > /dev/null

# Verify update
NEW_GOVERNOR=$(cat "$CURR_GOV_FILE")

# Confirm persistence setup
if whiptail --title "Persistence" --yesno "Current setting updated to '$NEW_GOVERNOR'.\n\nMake this persistent across reboots via systemd?" 10 65; then
    cat <<EOF > "$SERVICE_PATH"
[Unit]
Description=Set CPU Scaling Governor
After=multi-user.target

[Service]
Type=oneshot
ExecStart=/bin/sh -c 'echo $NEW_GOVERNOR | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor'
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
EOF

    systemctl daemon-reload
    systemctl enable set-cpu-governor.service
    
    whiptail --title "Success" --msgbox "Governor set to '$NEW_GOVERNOR'.\n\nSystemd service enabled:\n$SERVICE_PATH" 10 60
else
    # Remove persistence if user chooses runtime only
    if [ -f "$SERVICE_PATH" ]; then
        systemctl disable set-cpu-governor.service --now 2>/dev/null || true
        rm -f "$SERVICE_PATH"
        systemctl daemon-reload
    fi
    whiptail --title "Applied" --msgbox "Governor set to '$NEW_GOVERNOR' for this runtime only." 10 60
fi
