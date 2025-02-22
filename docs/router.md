# Router Documentation

The `Router` class is designed to manage routes and their associated templates. It provides methods to add, update, remove, and check the existence of routes, as well as properties to list and clear all routes. Below is a detailed explanation of the class, organized by properties and methods.

---

## Example Usage

```python
import pyweber as pw

def main(app: pw.Router):
    # Adding a route for the home page
    app.add_route(route='/', template=pw.Template(template='index.html'))

    # Adding a route for an "about" page
    app.add_route(route='/about', template=pw.Template(template='about.html'))

    # Adding a route for a "contact" page
    app.add_route(route='/contact', template=pw.Template(template='contact.html'))

    # Example of updating an existing route
    app.update_route(route='/about', template=pw.Template(template='about_new.html'))

    # Example of removing a route
    app.remove_route(route='/contact')

    # Checking if a route exists
    if app.exists(route='/about'):
        print("The route '/about' exists!")

    # Listing all registered routes
    print("Registered routes:", app.list_routes)

if __name__ == '__main__':
    # Starting the application with the `main` function
    pw.run(target=main)
```

## Properties

### `list_routes`
- **Type**: `list[str]`
- **Description**: Returns a list of all registered routes.
- **Usage**: This property is useful for retrieving all the routes that have been added to the router.

### `clear_routes`
- **Type**: `None`
- **Description**: Clears all registered routes from the router.
- **Usage**: Use this property to reset the router by removing all routes.

---

## Methods

### `add_route(route: str, template: Template) -> None`
- **Parameters**:
  - `route` (str): The route to be added. Must start with a `/`.
  - `template` (Template): The template associated with the route. Must be an instance of the `Template` class.
- **Description**: Adds a new route to the router. The route must start with a `/`, and the template must be an instance of the `Template` class. If the route already exists, a `ValueError` is raised.
- **Usage**: Use this method to register a new route with its corresponding template.

### `update_route(route: str, template: Template) -> None`
- **Parameters**:
  - `route` (str): The route to be updated.
  - `template` (Template): The new template to associate with the route. Must be an instance of the `Template` class.
- **Description**: Updates an existing route with a new template. If the route does not exist, a `ValueError` is raised. The template must be an instance of the `Template` class.
- **Usage**: Use this method to modify the template associated with an existing route.

### `remove_route(route: str) -> None`
- **Parameters**:
  - `route` (str): The route to be removed.
- **Description**: Removes a route from the router. If the route does not exist, a `ValueError` is raised.
- **Usage**: Use this method to delete a route from the router.

### `exists(route: str) -> bool`
- **Parameters**:
  - `route` (str): The route to check for existence.
- **Description**: Checks if a route exists in the router.
- **Returns**: `True` if the route exists, `False` otherwise.
- **Usage**: Use this method to verify if a route is already registered in the router.

### `redirect(from_route: str, to_route: str) -> str`
- **Parameters**:
  - `from_route` (str): The route from which to redirect.
  - `to_route` (str): The route to which to redirect.
- **Description**: Redirects from one route to another. If the `from_route` does not exist, a `ValueError` is raised. The method returns the rendered template of the `to_route`.
- **Usage**: Use this method to implement redirection logic between routes.

### `__get_route(route: str) -> str`
- **Parameters**:
  - `route` (str): The route to retrieve.
- **Description**: A private method that retrieves the rendered template for a given route. If the route does not exist, it returns an error template.
- **Returns**: The rendered template as a string.
- **Usage**: This method is used internally by the `redirect` method and should not be called directly.