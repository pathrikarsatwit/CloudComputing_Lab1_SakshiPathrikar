import requests

BASE_URL = "http://127.0.0.1:8080"  # This is where your FastAPI server runs

def driver():
    continueLoop = True
    while continueLoop:
        print("\nMy Driver")
        print("0) Exit")
        print("1) /home")
        print("2) /avengers")
        print("3) /villan")
        print("4) /avengername")
        print("5) /moviename")
        print("6) /villans")
        print("7) /gadget")
        print("8) /quotes")
        print("9) /quotesvillan")
        print("10) /yourAvenger")
        print("11) /verify-avenger")
        print("12) /welcome")
        userinput = input("Enter the route number you want to go to: ")


        if userinput == "0":
            continueLoop = False
            print("Exiting the driver. Goodbye!")

        elif userinput == "1":
            response = requests.get(f"{BASE_URL}/")
            print(response.json())

        elif userinput == "2":
            response = requests.get(f"{BASE_URL}/avengers")
            print(response.json())

        elif userinput == "3":
            response = requests.get(f"{BASE_URL}/villan")
            print(response.json())

        elif userinput == "4":
            name = input("Enter your favorite Avenger: ")
            response = requests.get(f"{BASE_URL}/avengername", params={"name": name})
            print(response.json())

        elif userinput == "5":
            movie = input("Enter your favorite Marvel movie: ")
            response = requests.get(f"{BASE_URL}/moviename", params={"movie": movie})
            print(response.json())

        elif userinput == "6":
            villans = input("Enter your favorite Villan: ")
            response = requests.get(f"{BASE_URL}/villans", params={"villans": villans})
            print(response.json())

        elif userinput == "7":
            gadgetName = input("Enter the gadget name: ")
            avenger = input("Enter the Avenger who uses this gadget: ")
            response = requests.get(f"{BASE_URL}/gadget/{gadgetName}/{avenger}")
            print(response.json())

        elif userinput == "8":
            avenger = input("Enter the Avenger's name to get their quote: ")
            response = requests.get(f"{BASE_URL}/quotes/{avenger}")
            print(response.json())

        elif userinput == "9":
            villansquotes = input("Enter the Villan's name to get their quote: ")
            response = requests.get(f"{BASE_URL}/quotesvillan/{villansquotes}")
            print(response.json())

        elif userinput == "10":
            response = requests.get(f"{BASE_URL}/yourAvenger")
            print(response.json())

        elif userinput == "11":
            avenger_code = input("Enter Avenger code: ")
            response = requests.get(f"{BASE_URL}/verify-avenger", headers={"x-avenger-code": avenger_code})
            print(response.json())

        elif userinput == "12":
            username = input("Enter your username: ")
            cookies = {'username': username}
            response = requests.get(f"{BASE_URL}/welcome", cookies=cookies)
            print(response.json())

        else:
            print("Enter a valid route number.")


if __name__ == "__main__":
    driver()
