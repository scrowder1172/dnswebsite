import dns.resolver
import dns.exception


def query_dns_records(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        for rdata in answers:
            print(f"{record_type} Record: {rdata.to_text()}")
    except dns.exception.DNSException as e:
        print(f"No {record_type} record found for {domain} or error occurred: {e}")


def main(domain):

    # Query various DNS record types
    record_types = {'A': 'Address',
                    'AAAA': 'Quad-A',
                    'CNAME': 'Canonical Name',
                    'MX': 'Mail Exchange',
                    'NS': 'Name Server',
                    'PTR': 'Pointer',
                    'TXT': 'Text',
                    'SRV': 'Service',
                    'SOA': 'Start of Authority',
                    'CAA': 'Certification Authority Authorization'}
    for key, item in record_types.items():
        print(f'\n****\n{item} Record:')
        query_dns_records(domain, key)


if __name__ == '__main__':
    domain_name = input('Domain name to search: ')
    main(domain=domain_name)
