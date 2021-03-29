# API Endpoints

## User 
### Register new Chef
* Type: POST
* URL: /api/chef/register/    (trailing forward slash is important)
* Data: 
    * first_name: string
    * last_name: string
    * email: string (email format)
    * password: string
    * about_me: string
    * location: string

### Login
* Type: POST
* URL: /api/chef/login/    (trailing forward slash is important)
* Data:
    * email: string (email format)
    * password: string
* Response:
    * success: Boolean
    * message: string
    
### Logout
* Type: POST
* URL: /api/chef/logout/    (trailing forward slash is important)
* Response:
    * success: Boolean
    * message: string
    
## Ingredient
### Create Ingredient
* Type: POST
* URL: /api/ingredient/    (trailing forward slash is important)
* Data: 
    * name: string
* Response:
    * ingredient_id: integer
    * name: string
    
### Get Ingredient by ID
* Type: GET
* URL: /api/ingredient/<ingredient_id>/    (trailing forward slash is important)
* Data: 
    * ingredient_id: integer
* Response:
    * ingredient_id: integer
    * name: string

## Recipe
### Create new Recipe
* Type: POST
* URL: /api/recipe/    (trailing forward slash is important)
* NOTE: Must be logged in to access. Duplicate recipes allowed. Only title, directions, ingredients are mandatory.
* Data: 
    * title: string
    * directions: string
    * prep_time: {"hours":integer, "minutes":integer}  
    * cook_time: {"hours":integer, "minutes":integer} 
    * total_time: {"hours":integer, "minutes":integer} 
    * serving_size: integer
    * nutritional_info: string
    * thumbnail_url: string (url format)
    * source: string (url format) 
    * ingredients: [{"name":string, "ingredient_string":string, "quantity":string, "unit":string}, ..., {}]
 * Response: Recipe JSON object
   
### Get Recipe by ID
* Type: GET
* URL: /api/recipe/<recipe_id>    (trailing forward slash is important)
* NOTE: Must be logged in to access. Duplicate recipes allowed. Only title, directions, ingredients are mandatory.
* Data: 
    * recipe_id: integer
* Response:
    * recipe_id: integer
    * title: string
    * directions: string
    * prep_time: {"hours":integer, "minutes":integer}  
    * cook_time: {"hours":integer, "minutes":integer} 
    * total_time: {"hours":integer, "minutes":integer} 
    * serving_size: integer
    * nutritional_info: string
    * thumbnail_url: string (url format)
    * source: string (url format) 
    * ingredients: [{"name":string, "ingredient_string":string, "quantity":string, "unit":string}, ..., {}]
