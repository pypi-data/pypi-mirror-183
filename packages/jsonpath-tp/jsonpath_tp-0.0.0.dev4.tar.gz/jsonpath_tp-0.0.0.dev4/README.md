
# The **jsonpath_tp** Package.

The **jsonpath_tp** is a [jsonpath](https://goessner.net/articles/JsonPath/) implementation built on top of 
[treepath](https://pypi.org/project/treepath/) technology.  Jsonpath is 
[query language](https://en.wikipedia.org/wiki/Query_language) for extracting data from 
[json](https://docs.python.org/3/library/json.html) document.   The jsonpath_tp attempts to follow the 
standard defined in 
[jsonpath](https://www.ietf.org/archive/id/draft-goessner-dispatch-jsonpath-00.html#name-detailed-definition) with 
the exceptions:
* script expression are not supported
* filter (script) expression define script differently in that a script is any single argument python function.
* filter expression support regular expression

The jsonpath_tp can be used programmatically or via th OS command line interface (CLI).   


# Quick Start Programmatically
All the jsonpath_tp components should be imported as follows:
```python
from jsonpath_tp import get, find
```

A jsonpath example that gets c's value from json data.

```python
data = {
    "a": {
        "b": [
            {
                "c": 1
            },
            {
                "c": 2
            }]
    }
}
value = get("$.a.b[0].c", data)
assert value == 1

```
A jsonpath example that gets c's value from json data.

```python
value = [value for value in find("$.a.b[*].c", data)]
assert value == [1, 2]
```
# Quick Start Command Line Interface
To use the cli install the jsonpath_tp python package in a venv:
```
python -m venv venv
source bin venv/bin/activate
pip install jsonpath_tp
```

A jsonpath example that gets  c's value from json data.

```python
pass
```

# Solar System Json Document

The examples shown in this README use the following json document.  It describes our solar system. Click to expand.  
<details><summary>solar_system = {...}</summary>
<p>

```json

{
  "star": {
    "name": "Sun",
    "diameter": 1391016,
    "age": null,
    "planets": {
      "inner": [
        {
          "name": "Mercury",
          "Number of Moons": "0",
          "diameter": 4879,
          "has-moons": false
        },
        {
          "name": "Venus",
          "Number of Moons": "0",
          "diameter": 12104,
          "has-moons": false
        },
        {
          "name": "Earth",
          "Number of Moons": "1",
          "diameter": 12756,
          "has-moons": true
        },
        {
          "name": "Mars",
          "Number of Moons": "2",
          "diameter": 6792,
          "has-moons": true
        }
      ],
      "outer": [
        {
          "name": "Jupiter",
          "Number of Moons": "79",
          "diameter": 142984,
          "has-moons": true
        },
        {
          "name": "Saturn",
          "Number of Moons": "82",
          "diameter": 120536,
          "has-moons": true
        },
        {
          "name": "Uranus",
          "Number of Moons": "27",
          "diameter": 51118,
          "has-moons": true
        },
        {
          "name": "Neptune",
          "Number of Moons": "14",
          "diameter": 49528,
          "has-moons": true
        }
      ]
    }
  }
}


```

</p>
</details>


# query examples.

| Description                                 | Xpath                               | jsonpath                                  | treepath                            |
|----------------------------------------------|-------------------------------------|-------------------------------------------|------------------------------------|
| Find planet earth.                           | /star/planets/inner[name='Earth']   | $.star.planets.inner[?(@.name=='Earth')]  | path.star.planets.inner[*][?(@.name == 'Earth')]   |
| List the names of all inner planets.         | /star/planets/inner[*].name         | $.star.planets.inner[*].name              | path.star.planets.inner[*].name   |
| List the names of all planets.               | /star/planets/*/name                | $.star.planets.*[*].name                   | path.star.planets.wc[*].name      |
| List the names of all celestial bodies       | //name                              | $..name                                   | path.rec.name                      |  
| List all nodes in the tree Preorder          | //*                                 | $..                                       | path.rec                           |
| Get the third rock from the sun              | /star/planets/inner[3]              | $.star.planets.inner[2]                   | path.star.planets.inner[2]         |
| List first two inner planets                 | /star/planets.inner[position()<3]   | $.star.planets.inner[:2]                  | path.star.planets.inner[0:2]       |
|                                              |                                     | $.star.planets.inner[0, 1]                | path.star.planets.inner[0, 2]      |
| List planets smaller than earth              | /star/planets/inner[diameter < 1]   | $.star.planets.inner[?(@.diameter < 12756)]              | path.star.planets.inner[wc][has(path.diameter < 12756)]      |
| List celestial bodies that have planets.     | //*[planets]/name                   | $..[?(@.planets)].name                   | path.rec[?(@.planets)].name       |
| List the planets with more than 50 moons     |                                     | $..[?(int(@['Number of Moons']) > 50)].name | path.rec[wc][has(path['Number of Moons'] > 50, int)].name |


# Traversal Functions
## get
The **get** function returns the first value the path leads to.

Get the star name from the solar_system

```python
sun = get("$.star.name", solar_system)
assert sun == 'Sun'

```
When there is no match, MatchNotFoundError is thrown.

```python
try:
    get("$.star.human_population", solar_system)
    assert False, "Not expecting humans on the sun"
except MatchNotFoundError:
    pass

```
Or if preferred, a default value can be given.

```python
human_population = get("$.star.human_population", solar_system, default=0)
assert human_population == 0

```
In addition to a constant, the default value may also be a callable

```python
def population():
    return 0

human_population = get("$.star.human_population", solar_system, default=population)
assert human_population == 0

```
The default value can be automatically injected in to json document

```python
human_population = get("$.star.human_population", solar_system, default=1, store_default=True)
assert human_population == solar_system['star']["human_population"]
```
## find
The **find** function returns an Iterator that iterates to each value the path leads to.  Each value is
determine on its iteration.

Find All the planet names.

```python
inner_planets = [planet for planet in find("$.star.planets.inner[*].name", solar_system)]
assert inner_planets == ['Mercury', 'Venus', 'Earth', 'Mars']
```
## Tracing Debugging
All the functions: get, find, support tracing.   An option, when enabled,
records the route the algorithm takes to determine a match.

This example logs the route the algorithm takes to find the inner planets.  The **print**
function is give to capture the logs, but any single argument function can be used.

```python
inner_planets = [planet for planet in find("$.star.planets.inner[*].name", solar_system, trace=log_to(print))]
assert inner_planets == ['Mercury', 'Venus', 'Earth', 'Mars']

```
The results

```python
"""
at $.star got {'name': 'Sun', 'dia...
at $.star.planets got {'inner': [{'name': ...
at $.star.planets.inner got [{'name': 'Mercury',...
at $.star.planets.inner[*] got {'name': 'Mercury', ...
at $.star.planets.inner[0].name got 'Mercury'
at $.star.planets.inner[*] got {'name': 'Venus', 'N...
at $.star.planets.inner[1].name got 'Venus'
at $.star.planets.inner[*] got {'name': 'Earth', 'N...
at $.star.planets.inner[2].name got 'Earth'
at $.star.planets.inner[*] got {'name': 'Mars', 'Nu...
at $.star.planets.inner[3].name got 'Mars'
"""
```
# Path
## The root
The **$** point to root of the tree.

```python
value = get("$", solar_system)

assert value == solar_system

```
In a filter, the **@**  point to the current element.

```python
value = get("$.star[?(@ == 'Sun')]", solar_system)

assert value == 'Sun'
```
## Dictionaries
### Keys
The dictionary keys are referenced as dynamic attributes on a path.

```python
inner_from_attribute = get("$.star.planets.inner", solar_system)
inner_from_string_keys = get("$.['star']['planets']['inner']", solar_system)

assert inner_from_attribute == inner_from_string_keys == solar_system['star']['planets']['inner']
```
### Keys With Special Characters
Dictionary keys that are not valid python syntax can be referenced as quoted strings.

```python
sun_equatorial_diameter = get("$.star.planets.inner[0]['Number of Moons']", solar_system)

assert sun_equatorial_diameter == solar_system['star']['planets']['inner'][0]['Number of Moons']
```
### Wildcard as a Key.
The * attribute specifies all sibling keys.   It is useful for iterating over attributes.

```python
star_children = [child for child in find("$.star.*", solar_system)]
assert star_children == [solar_system['star']['name'],
                         solar_system['star']['diameter'],
                         solar_system['star']["age"],
                         solar_system['star']['planets'], ]
```
### Comma Delimited Keys
Multiple dictionary keys can be specified using a comma delimited list.

```python
last_and_first = [planet for planet in find("$.star['diameter', 'name']", solar_system)]
assert last_and_first == [1391016, "Sun"]
```
## List
### Indexes
List can be access using index.

```python
earth = get("$.star.planets.inner[2]", solar_system)
assert earth == solar_system['star']['planets']['inner'][2]

```
List the third inner and outer planet.

```python
last_two = [planet for planet in find("$.star.*.*[2].name", solar_system)]
assert last_two == ['Earth', 'Uranus']
```
### Comma Delimited Indexes.
List indexes can be specified as a comma delimited list.

```python
last_and_first = [planet for planet in find("$.star.planets.outer[3, 0].name", solar_system)]
assert last_and_first == ["Neptune", "Jupiter"]
```
### Slices
List can be access using slices.

List the first two planets.

```python
first_two = [planet for planet in find("$.star.planets.outer[:2].name", solar_system)]
assert first_two == ["Jupiter", "Saturn"]

```
List the last two planets.

```python
last_two = [planet for planet in find("$.star.planets.outer[-2:].name", solar_system)]
assert last_two == ["Uranus", "Neptune"]

```
List all outer planets in reverse.

```python
last_two = [planet for planet in find("$.star.planets.outer[::-1].name", solar_system)]
assert last_two == ["Neptune", "Uranus", "Saturn", "Jupiter"]

```
List the last inner and outer planets.

```python
last_two = [planet for planet in find("$.star.*.*[-1:].name", solar_system)]
assert last_two == ["Mars", "Neptune"]
```
### Wildcard as an Index.
The * token can be used as a list index.   It is useful for iterating over attributes.

```python
all_outer = [planet for planet in find("$.star.planets.outer[*].name", solar_system)]
assert all_outer == ["Jupiter", "Saturn", "Uranus", "Neptune"]
```
## Recursion
The .. double dot implies recursive search.  It executes a preorder tree traversal.  The search algorithm
descends the tree hierarchy evaluating the path on each vertex until a match occurs.  On each iteration it
continues where it left off. This is an example that finds all the planets names.

```python
all_planets = [p for p in find("$.star.planets..name", solar_system)]
assert all_planets == ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

```
Here is another example that finds all the celestial bodies names.

```python
all_celestial_bodies = [p for p in find("$..name", solar_system)]
assert all_celestial_bodies == ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus',
                                'Neptune']
```
## Filters

Filters are use to add additional search criteria.

### filter 
The ?() is a filter that evaluates a branched off path relative to its parent path.  This example
finds all celestial bodies that have planets.

```python
sun = get("$..[?(@.planets)].name", solar_system)
assert sun == "Sun"

```
This search finds all celestial bodies that have a has-moons attribute.

```python
all_celestial_bodies_moon_attribute = [planet for planet in find("$..[?(@['has-moons'])].name", solar_system)]
assert all_celestial_bodies_moon_attribute == ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus',
                                               'Neptune']

```
This search finds all celestial bodies that have moons. Note the **operator.truth** is used to exclude planets
that don't have moons.

```python
operator_truth = operator.truth
all_celestial_bodies_moon_attribute = [planet for planet in
                                       find("$..[?(operator_truth(@['has-moons']))].name",
                                            solar_system,
                                            locals=locals()
                                            )]
assert all_celestial_bodies_moon_attribute == ['Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
```
### has filter comparison operators
Filters can be specified with a comparison operator.

```python
earth = [planet for planet in find("$..[?(@.diameter == 12756)].name", solar_system)]
assert earth == ['Earth']

earth = [planet for planet in find("$..[?(@.diameter != 12756)].name", solar_system)]
assert earth == ['Sun', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

earth = [planet for planet in find("$..[?(@.diameter > 12756)].name", solar_system)]
assert earth == ['Sun', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

earth = [planet for planet in find("$..[?(@.diameter >= 12756)].name", solar_system)]
assert earth == ['Sun', 'Earth', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

earth = [planet for planet in find("$..[?(@.diameter < 12756)].name", solar_system)]
assert earth == ['Mercury', 'Venus', 'Mars']

earth = [planet for planet in find("$..[?(@.diameter <= 12756)].name", solar_system)]
assert earth == ['Mercury', 'Venus', 'Earth', 'Mars']

```
There is also a regular expression operator.   This example finds
all the planets that end with the letter s.

```python
earth = [planet for planet in find(r"$..[?(@.name =~ '\w+s')].name", solar_system)]
assert earth == ['Venus', 'Mars', 'Uranus']
```
### has filter type conversion
Sometimes the value is the wrong type for the comparison operator. In this example the attribute
'Number of Moons' is str type.

```python
planets = [planet for planet in find("$..[?(@['Number of Moons'] > '5')].name", solar_system)]
assert planets == ['Jupiter', 'Saturn']

```
This is how to convert the type to an int before applying the comparison operator.

```python
planets = [planet for planet in find("$..[?(int(@['Number of Moons']) > 5)].name", solar_system)]
assert planets == ['Jupiter', 'Saturn', 'Uranus', 'Neptune']
```
### has filter comparison operators as single argument functions
A filter operator can be specified as a single argument function.  Here an example that searches for planets that
have the same diameter as earth.

```python
earths_diameter = partial(operator.eq, 12756)
earth = [planet for planet in find("$..[?(earths_diameter(@.diameter))].name", solar_system, locals=locals())]
assert earth == ['Earth']

```
Any single argument function can be used as an operator.  This example uses a Regular Expression to finds
planets that end with the letter s.

```python
name_ends_with_s = re.compile(r"\w+s").match
earth = [planet for planet in find("$..[?(name_ends_with_s(@.name))].name", solar_system, locals=locals())]
assert earth == ['Venus', 'Mars', 'Uranus']

```
This example uses a closure to find planets that have the same diameter as earth.

```python
def smaller_than_earth(value):
    return value < 12756

earth = [planet for planet in find("$..[?(smaller_than_earth(@.diameter))].name", solar_system, locals=locals())]
assert earth == ['Mercury', 'Venus', 'Mars']
```
### logical and, or and not filters
#### and
A regular express to test if the second letter in the value is 'a'.

```python
second_letter_is_a = re.compile(r".a.*").fullmatch

```
The **and** function evaluates as the logical **and** operator.   It is equivalent to: (arg1 and arg2 and ...)

```python
found = [planet for planet in find("$..[?(@.diameter < 10000 and (second_letter_is_a(@.name)))].name",
                                   solar_system,
                                   locals=locals())
         ]
assert found == ['Mars']

```
#### or
The **or** function evaluates as the logical **or** operator.   It is equivalent to: (arg1 and arg2 and ...)

```python
found = [planet for planet in find("$..[?(@.diameter < 10000 or (second_letter_is_a(@.name)))].name",
                                   solar_system,
                                   locals=locals()
                                   )
         ]
assert found == ['Mercury', 'Earth', 'Mars', 'Saturn']

```
#### not
The **not** function evaluates as the logical **not** operator.   It is equivalent to: (not arg)
This example find all the planets names not not equal to Earth.  Note the double nots.

```python
found = [planet for planet in find("$..[?(not (@.name != 'Earth'))].name", solar_system)]
assert found == ['Earth']

```
#### Combining has, and, or, and not filters.
Each of the **has** function can be passed as arguments to any of the other **has** function to construct complex
boolean equation.  This example is equivalent to:
(10000 > diameter  or diameter > 20000) and second_letter_is_a(name))

```python
found = [planet for planet in
         find("$..[?((@.diameter < 10000 or @.diameter > 20000) and (second_letter_is_a(@.name)))].name",
              solar_system,
              locals=locals()
              )
         ]
assert found == ['Mars', 'Saturn']
```
