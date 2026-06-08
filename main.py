import argparse
from query import DNS_Whisperer


def main():
    parser = argparse.ArgumentParser(description="DNS Lookup")
    parser.add_argument("--domain", "-d", help="--domain DOMAIN")
    parser.add_argument("--record", "-r", help="--record RECORD (A, MX, TXT, etc.)")

    args = parser.parse_args()
    resolver = DNS_Whisperer(args.domain, args.record)
    resolver.lookup() 

    if not args.domain or not args.record:
        parser.print_help()
        return

if __name__ == "__main__":
    main()
