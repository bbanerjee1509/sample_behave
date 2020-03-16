# file:features/omdb_search.feature
Feature: Movie Search
    Scenario Outline:Search Movie in Open Movie Database
    Given I want to search movie name "<movie_name>"
    When I send the search request
	Then response should return integer "http_response_code" : "200"
	Then response should contain "<movie_name>" in "Title"
	Then response should contain "<year>" in "Year"


	Examples:Movies - <movie_name>
        | movie_name     |  year |
        | Forrest Gump   |  1994 |
        | Terminator     |  2001 |
        | Friends        |  2007 |