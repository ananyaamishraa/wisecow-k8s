from collections import Counter

LOG_FILE = "access.log"

def analyze_logs(log_file):
    ip_counter = Counter()
    page_counter = Counter()
    error_404_count = 0

    with open(log_file, "r") as file:
        for line in file:
            parts = line.split()

            if len(parts) < 9:
                continue

            ip_address = parts[0]
            requested_page = parts[6]
            status_code = parts[8]

            ip_counter[ip_address] += 1
            page_counter[requested_page] += 1

            if status_code == "404":
                error_404_count += 1

    return ip_counter, page_counter, error_404_count

def print_report(ip_counter, page_counter, error_404_count):
    print("\n===== LOG ANALYSIS REPORT =====\n")

    print(f"Total 404 Errors: {error_404_count}\n")

    print("Top 5 Most Requested Pages:")
    for page, count in page_counter.most_common(5):
        print(f"{page} → {count} requests")

    print("\nTop 5 IP Addresses by Request Count:")
    for ip, count in ip_counter.most_common(5):
        print(f"{ip} → {count} requests")

def main():
    ip_counter, page_counter, error_404_count = analyze_logs(LOG_FILE)
    print_report(ip_counter, page_counter, error_404_count)

if __name__ == "__main__":
    main()
