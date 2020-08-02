import csv
from link_downloader import login_to_thrive, get_customer_link, quit_chrome


# Extract customer id, and email to emails.csv
def extract_emails():
    with open('emails.csv', mode='w') as email_file:
        with open('customer_download.csv', mode='r') as download_file:
            csv_reader = csv.DictReader(download_file)
            csv_writer = csv.writer(email_file)
            line_count = 0

            for row in csv_reader:
                email = 'Email'
                customer_id = 'Customer ID'
                url = 'Url'


                if line_count != 0:
                    email = row['Email']
                    customer_id = row['Customer ID']
                    url = ''
                    
                csv_writer.writerow([customer_id, email,url])

                line_count += 1

    print(f'Wrote {line_count} lines to emails.csv')

# Loops through emails.csv and tries to add customer referral links
def hydrate_email_list():
    with open('emails.csv', mode='r') as email_file:
        with open('final.csv', mode='w') as final_file:
            csv_reader = csv.DictReader(email_file)
            csv_writer = csv.writer(final_file)
            line_count = 0
            for row in csv_reader:
                customer_id = row ['Customer ID']
                url = row['Url']
                email = row['Email']

                if url == '':
                    print (f'[{line_count}/{14897}] Getting referral link for customer: {email} ({customer_id})')
                    url = get_customer_link(customer_id)
                    csv_writer.writerow([customer_id, email, url])
                    
                else:
                    print (f'Skipping {email} as this individual already has a url: {url}')

                line_count += 1


def main():
    login_to_thrive()
    hydrate_email_list()
    quit_chrome()


main()
print ('All done!')
