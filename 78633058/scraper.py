DOMAIN = "www.amazon.co.uk"
PATH = "HyperX-Cloud-III-Wireless-microphone/product-reviews/B0CBQXGZ85/ref=cm_cr_arp_d_viewopt_sr"

STARS = ["one", "two", "three", "four", "five"]

for page in range(1, 11):
    for stars in STARS:
        params = f"pageNumber={page}&filterByStar={stars}_star"

        URL = f"https://{DOMAIN}/{PATH}/?{params}"
        print(URL)