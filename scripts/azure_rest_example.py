import argparse
import os
import requests


def build_request(subscription_id, resource_group):
    return {
        "method": "GET",
        "url": (
            "https://management.azure.com/subscriptions/"
            f"{subscription_id}/resourcegroups/{resource_group}"
        ),
        "api_version": "2021-04-01",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID", "example-subscription")
    resource_group = os.getenv("AZURE_RESOURCE_GROUP", "example-resource-group")
    request_info = build_request(subscription_id, resource_group)

    if args.dry_run:
        print(request_info)
        return

    token = os.getenv("AZURE_ACCESS_TOKEN")
    if not token:
        raise SystemExit("Set AZURE_ACCESS_TOKEN before making a live request.")

    response = requests.get(
        request_info["url"],
        params={"api-version": request_info["api_version"]},
        headers={"Authorization": f"Bearer {token}"},
        timeout=20,
    )
    response.raise_for_status()
    print(response.json())


if __name__ == "__main__":
    main()
