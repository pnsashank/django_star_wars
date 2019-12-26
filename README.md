#star_Wars
List of commands to run:
```
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver```

'Planets' app of star_Wars project, fetches data from "swapi"(Star Wars API), based on the planet_name given by the end user via a form

The Form consists of the input field along with a submit button to enter their favorite planet name in Star Wars Universe to get planet details. The planet details displayed in the results page include: planet_name, rotation_period, orbital_period, gravity.

The application consists of a local store, which holds information about planet_name, rotation_period, orbital_period, gravity, films and a default image in the database named Planet with the above mentioned attributes (sqlite3 database is used). Achieved through the use of add button, in the results page when the planet name is submitted.

swapi does not provide any images for the planets, hence the use of a default image.

The application initially checks, whether the data is in the local store. If so the data from the local store is extracted and displayed. This is performed under the assumption that the data is static.

If the planet_name is not present in the local store, an API call is made to swapi. The JSON data from swapi API is parsed to extract the details if the planet present in the 'results' key of the JSON. If a wrong planet name is typed in, the swapi API return the 'results' key with planet names in its database, via string matching.

######Additional Feature added:

If the planet_name is not present in swapi JSON result, then it is assumed that the user has typed in the wrong planet name. Here, approximate string matching of the planet_name is done with the use of fuzzywuzzy library, using the token_sort_ratio() method, with the exisiting planet names in the local store.

token_sort_ratio() method works by taking into account, similar strings that are out of order. The planet names in the local store are compared to the submitted planet_name and the ratios are compared. The planet name with the highest matching ratio is assumed to be what the user intended to type and the result for that planet_name is published.

The use of approximate string matching brings in an additional feature, which acts as a check over the submitted data, allowing the end-user to have a seamless experience.

######Other Additional Features that can be added:

It is assumed that the data in swapi is static. If the data changes over time, instead of publishing exisiting data in the local store, an API call is made to check for updated values and the local store attributes are updated accordingly along with the updated planet details being published.

The application can help users create accounts,so that each user can have personalised access to the application features, like unique local stores.
