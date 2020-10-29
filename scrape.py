import bs4
import requests
link = "https://www.ebay.com/sch/i.html?Card%2520Attributes=Rookie&Product=Single&Grade=%2521%7CUngraded&_sacat=214&_nkw=jaxson+hayes+prizm+base+rookie&LH_Complete=1&_dcat=214&LH_Sold=1&_fcid=1&_sop=13"


def scrapePage(page):
    r = requests.get(page)
    data = r.text
    soup = bs4.BeautifulSoup(data)
    listings = soup.find_all('li', attrs={'class': 's-item'})

    for listing in listings:
        name = ""
        link = ""
        purchase_type = ""
        bids = ""
        shipping_cost = ""
        sale_date = ""
        image = ""
        price = ""

        for n in listing.find_all('h3', attrs={'class': "s-item__title"}):
            name = n.text
            print("name: ", name)
        for l in listing.find_all('a', attrs={'class': "s-item__link"}):
            link = l['href'].split("?", 1)[0]
            print("link: ", link)
        for pt in listing.find_all('span', attrs={'class': "s-item__purchase-options-with-icon"}):
            purchase_type = pt.text
            print("purchase_type: ", purchase_type)
        for p in listing.find_all('span', attrs={'class': "s-item__price"}):
            # Handle the following possible output types:
            # Price Range: [<span class="POSITIVE">$0.99</span>, <span class="DEFAULT POSITIVE"> to </span>, <span class="POSITIVE">$54.99</span>]
            # Offer Accepted: [<span class="STRIKETHROUGH POSITIVE">$5.00</span>]
            # Actual Price: [<span class="POSITIVE">$7.45</span>]
            # print("price: ", price.findChildren())
            if len(p.findChildren()) > 1:
                for pr in p.findChildren():
                    price += pr.text
                print("price: ", price)
            else:
                price = p.findChildren()[0].text
                print("price: ", price)
        for b in listing.find_all('span', attrs={'class': "s-item__bids"}):
            bids = b.text
            print("bids: ", bids)
        for sc in listing.find_all('span', attrs={'class': "s-item__shipping"}):
            shipping_cost = sc.text
            print("shipping_cost: ", shipping_cost)
        for sd in listing.find_all('span', attrs={'class': "s-item__ended-date"}):
            sale_date = sd.text
            print("sale_date: ", sale_date)
        for i in listing.find_all('img', attrs={'class': "s-item__image-img"}):
            image = i['src']
            print("image: ", image)
        print("\n")
