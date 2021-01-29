from craigslist import CraigslistForSale
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker
from dateutil.parser import parse
from util import post_listing_to_slack
from slack import WebClient
import time
import settings

engine = create_engine('sqlite:///listings.db', echo=False)

Base = declarative_base()

class Listing(Base):
    """
    A table to store data on craigslist listings.
    """

    __tablename__ = 'listings'

    id = Column(Integer, primary_key=True)
    link = Column(String, unique=True)
    created = Column(DateTime)
    #geotag = Column(String)
    #lat = Column(Float)
    #lon = Column(Float)
    name = Column(String)
    price = Column(Float)
    location = Column(String)
    cl_id = Column(Integer, unique=True)
    #area = Column(String)
    #bart_stop = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def scrape_area(query):
    """
    Scrapes craigslist for a certain geographic area, and finds the latest listings.
    :param area:
    :return: A list of results.
    """
    print(query["section"]);

    cl_f = CraigslistForSale(site="minneapolis",
                            area=["hnp", "ram", "ank", "wsh", "dak", "csw"],
                            category=query['section'],
                            filters={
                                "query":query["query"],
                                "min_price":query["min_price"],
                                "max_price":query["max_price"]
                            })
    results = []
    gen = cl_f.get_results(sort_by="newest", limit=10)
    while True:
        try:
            result = next(gen)
        except StopIteration:
            break
        except Exception:
            continue
        listing = session.query(Listing).filter_by(cl_id=result["id"]).first()

        # Don't store the listing if it already exists.
        if listing is None:
            # if result["where"] is None:
            #     # If there is no string identifying which neighborhood the result is from, skip it.
            #     continue
            # lat = 0
            # lon = 0
            # if result["geotag"] is not None:
            #     # Assign the coordinates.
            #     lat = result["geotag"][0]
            #     lon = result["geotag"][1]
            #
            #     # Annotate the result with information about the area it's in and points of interest near it.
            #     geo_data = find_points_of_interest(result["geotag"], result["where"])
            #     result.update(geo_data)
            # else:
            #     result["area"] = ""
            #     result["bart"] = ""

            # Try parsing the price.
            price = 0
            try:
                price = float(result["price"].replace("$", ""))
            except Exception:
                pass

            # result["area"] = None
            # result[]

            # Create the listing object.
            listing = Listing(
                link=result["url"],
                created=parse(result["datetime"]),
                #lat=lat,
                #lon=lon,
                name=result["name"],
                price=price,
                location=result["where"],
                cl_id=result["id"]
                #area=None,#result["area"],
                #bart_stop=None#result["bart"]
            )

            # Save the listing so we don't grab it again.
            session.add(listing)
            session.commit()

            results.append(result)
            # Return the result if it's near a bart station, or if it is in an area we defined.
            # if len(result["bart"]) > 0 or len(result["area"]) > 0:
            #     results.append(result)

    return results

def do_scrape():
    """
    Runs the craigslist scraper, and posts data to slack.
    """

    # Create a slack client.
    sc = WebClient(settings.SLACK_TOKEN)

    # Get all the results from craigslist.
    for query in settings.FURNITURE_QUERIES:
        results = scrape_area(query)
        for result in results:
            post_listing_to_slack(sc, result, query["slack_channel"])
        time.sleep(10)


    # for area in settings.AREAS:
    #     all_results += scrape_area(area)
    #
    # for result in all_results:
    #     print(result)

    #print("{}: Got {} results".format(time.ctime(), len(all_results)))

    # Post each result to slack.
    # for result in all_results:
    #    post_listing_to_slack(sc, result)
