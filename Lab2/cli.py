# cli.py

import argparse
import requests

BASE_URL = "http://localhost:8080"

def main():
    parser = argparse.ArgumentParser(description="Marvel Command Line Interface")

    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # 1. Root route ("/")
    subparsers.add_parser("home", help="Hello, Welcome to Marvel!")

    # 2. /avengers route: list all Avengers
    subparsers.add_parser("avengers", help="List all Avengers")
    
    # 3. /villan route: list all Villains
    subparsers.add_parser("villan", help="List all Villans")

    # 4. /avengername?name= route
    name_parser = subparsers.add_parser("avengername", help="Set your favorite Avenger")
    name_parser.add_argument("--name",required=True, help="Your favorite Avenger's name")

    # 5. /moviename?movie= route
    movie_parser = subparsers.add_parser("moviename", help="Set your favorite Marvel movie")
    movie_parser.add_argument("--movie", required=True, help="Your favorite Marvel movie")

    # 6. /villans?villans= route (set your favorite villain)
    fav_villain_parser = subparsers.add_parser("villans", help="Set your favorite Villan")
    fav_villain_parser.add_argument("--villan",required=True, help="Name of the Villan")
    
    # 7. /quotes/{avenger} route
    quote_avenger_parser = subparsers.add_parser("quote-avenger", help="Get a quote from an Avenger")
    quote_avenger_parser.add_argument("--avenger", required=True, help="Name of the Avenger")
    
    # 8. /quotesvillan/{villansquotes} route
    quote_villain_parser = subparsers.add_parser("quote-villans", help="Get a quote from a Villian")
    quote_villain_parser.add_argument( "--villan", required=True, help="Name of the Villian")

    # 9. /gadget/{gadgetName}/{avenger} route
    gadget_parser = subparsers.add_parser("gadget", help="Get a gadget info")
    gadget_parser.add_argument("--gadgetName", required=True, help="Name of the gadget")
    gadget_parser.add_argument("--avenger", required=True, help="Name of the Avenger")
    
    # 10. /yourAvenger route
    subparsers.add_parser("yourAvenger", help="List your saved Avenger info")
    
    # 11. /verify-avenger via header
    verify_parser = subparsers.add_parser("verify-avenger", help="Verify if user is an Avenger via header")
    verify_parser.add_argument("--code", required=True, help="Secret Avenger header code")

    # 12. /welcome via cookie
    welcome_parser = subparsers.add_parser("welcome", help="Welcome user with cookie")
    welcome_parser.add_argument("--username", required=True, help="Username to pass in cookie")


    args = parser.parse_args()

    if args.command == "home":
        response = requests.get(f"{BASE_URL}/")
        print(response.text)

    elif args.command == "avengers":
        response = requests.get(f"{BASE_URL}/avengers")
        print(response.json())

    elif args.command == "villan":
        response = requests.get(f"{BASE_URL}/villan")
        print(response.json())

    elif args.command == "avengername":
        response = requests.get(
            f"{BASE_URL}/avengername", 
            params={"name": args.name}
        )
        print(response.text)

    elif args.command == "moviename":
        response = requests.get(
            f"{BASE_URL}/moviename", 
            params={"movie": args.movie}
        )
        print(response.text)

    elif args.command == "villans":
        response = requests.get(
            f"{BASE_URL}/villans", 
            params={"villans": args.villan}  
        )
        print(response.text)

    elif args.command == "quote-avenger":
        response = requests.get(
            f"{BASE_URL}/quotes/{args.avenger}"
        )
        print(response.text)

    elif args.command == "quote-villans":
        response = requests.get(
            f"{BASE_URL}/quotesvillan/{args.villan}"
        )
        print(response.text)

    elif args.command == "gadget":
        response = requests.get(
            f"{BASE_URL}/gadget/{args.gadgetName}/{args.avenger}"
        )
        print(response.text)

    elif args.command == "yourAvenger":
        response = requests.get(f"{BASE_URL}/yourAvenger")
        print(response.json())

    elif args.command == "verify-avenger":
        headers = {"X-Avenger-Code": args.code}
        response = requests.get(
            f"{BASE_URL}/verify-avenger", 
            headers=headers
        )
        print(response.json())

    elif args.command == "welcome":
        cookies = {"username": args.username}
        response = requests.get(
            f"{BASE_URL}/welcome", 
            cookies=cookies
        )
        print(response.json())

if __name__ == "__main__":
    main()
