class scrape_rounds:
    # Import necessary modules
    import cloudscraper
    import time
    from fake_useragent import UserAgent
    import threading
    # Create a Cloudflare scraper and a fake user agent
    scraper = cloudscraper.create_scraper()
    ua = UserAgent()
    # Initialize the last round variable to an empty string
    last_round = ""

    def gather_round_data():
        # The URL for the API to get data on the current round
        api_url = "https://rest-bf.blox.land/games/crash"
        try:
            # Make a request to the API and get the response in JSON format
            round_data = scrape_rounds.scraper.get(api_url, headers = {'User-Agent': scrape_rounds.ua.chrome}).json()
            # Get the crash point from the response data
            crash_point = round_data["history"][0]["crashPoint"]
            global last_round
            # Check if the current round is different from the last round
            if round_data["history"][0]["privateSeed"] != scrape_rounds.last_round:
                # Update the last round variable
                scrape_rounds.last_round = round_data["history"][0]["privateSeed"]
                # Return the crash point
                return crash_point
            else:
                # Return False if the current round is the same as the last round
                return False
        except Exception as e:
            # Raise an exception if the request to the API failed
            raise Exception("Failed to bypass Cloudflare")
    
    def gather_data(num_rounds):
        # Initialize the variable to keep track of the number of rounds gathered
        num_rightnow = 0
        # Open the file for appending
        with open('crash_data.csv', 'a') as f:
            # Keep gathering data until the desired number of rounds has been reached
            while num_rounds >= num_rightnow:
                # Get the data for the current round
                round_data = scrape_rounds.gather_round_data()
                # If the round data is not False (i.e., it is not the same as the last round)
                if round_data != False:
                    # Write the data to the file
                    f.write(str(round_data) + '\n')
                    # Increment the number of rounds gathered
                    num_rightnow += 1
    
    def reset():
        # Open the file for writing and clear its contents
        with open('crash_data.csv', 'w') as f:  
            f.write("")  
        return "resetted data"           
