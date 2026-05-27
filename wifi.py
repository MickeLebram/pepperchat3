import platform
import subprocess


def list_wifi_networks():
    system = platform.system()

    try:
        if system == "Linux":
            result = subprocess.run(
                ["nmcli", "-t", "-f", "SSID", "dev", "wifi"],
                capture_output=True,
                text=True
            )
            return sorted(set(
                ssid for ssid in result.stdout.splitlines() if ssid
            ))

        elif system == "Windows":
            result = subprocess.run(
                ["netsh", "wlan", "show", "networks"],
                capture_output=True,
                text=True
            )

            networks = []
            for line in result.stdout.splitlines():
                if "SSID" in line and "BSSID" not in line:
                    ssid = line.split(":", 1)[1].strip()
                    if ssid:
                        networks.append(ssid)

            return sorted(set(networks))

        elif system == "Darwin":  # macOS
            airport = (
                "/System/Library/PrivateFrameworks/"
                "Apple80211.framework/Versions/Current/Resources/airport"
            )

            result = subprocess.run(
                [airport, "-s"],
                capture_output=True,
                text=True
            )

            networks = []
            lines = result.stdout.splitlines()[1:]  # skip header

            for line in lines:
                parts = line.split()
                if parts:
                    networks.append(parts[0])

            return sorted(set(networks))

        else:
            raise RuntimeError(f"Unsupported OS: {system}")

    except Exception as e:
        return [f"Error: {e}"]


print(list_wifi_networks())