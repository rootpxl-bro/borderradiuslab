"""Minimal example for BorderRadiusLab."""

from borderradiuslab import borderradiuslab


def main():
 runner = borderradiuslab({"name": "BorderRadiusLab", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()