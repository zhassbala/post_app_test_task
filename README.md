# post_app_test_task
This is a test task API that implements Post App with authorization, tags and basic CRUD operations.

base url: https://post-app-test.herokuapp.com/

## Endpoints

* `/api/login/`: Takes `username` and `password` as 
                 parameters, logs in the user and 
                 returns an authorization token. 
                 If the user is not registered, 
                 returns 404 response and shows an appropriate message'

* `/api/register/`: Takes `username`, `email` and `password` as parameters, 
                    and registers the user after validation. 
                    In case of failed validation (username already in use, etc.),
                    responds with an appropriate message.

* `/api/post_create`: creates a post with given `title`, `content`, and an array of `tags`

* `/api/post_update`: updates a post. Takes one required argument `id` and three optional arguments: `title`, `content`, `tags`

* `/api/post_delete`: deletes a post with given `id` if the user can access it. Otherwise gives an error.

* `/api/get_posts_by_tags,`: Filters posts according to given tags. Takes one required argument `tags` - an array of tags for search 
    > Ex. `["Kazakhstan, Education, IT"]`, etc. 

    Can also take one optional boolean argument `intersection` - if true, returns posts that have **all** the given tags; if false, returns posts that have **at least one** of the given tags. By default is false.

* `/api/get_posts_by_date,`: Filters posts based on `date_added` field of the post, can take `from` and `until` arguments, both are date strings and both are optional. If no argument provided, returns posts from 01.01.1970 until now.

* `/api/get_user`: Returns `id`, `username` and `email` of the logged user

* `/api/my_posts`: Returns the posts that are created by logged user
