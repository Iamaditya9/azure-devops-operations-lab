from app.services.config_validator import missing_variables


def main():
    missing = missing_variables()
    if missing:
        print("Missing configuration:")
        for item in missing:
            print(f"- {item}")
        raise SystemExit(1)
    print("Environment configuration is valid.")


if __name__ == "__main__":
    main()
