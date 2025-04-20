# Recipe CLI app

## First step

- First thing I need to do is figure out the format I want to use for this project
- One thing I thought about is doing it similarly to my C# terminal app where you could select options with the arrow keys
- Then you could input the data you wanted
- Another thing is to figure out how to call the API and how to format the request
  - Example:
    - https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+flour,+sugar&number=2
    - Problem is that how ingredients are added into the path
- Another thing I want to try is to setup a virtual environment
  - Similarly to the one in Bosch, but not with conda.
  - requirements.txt
- Git tracking -> public repo (make sure .env files are not pushed by default)

## Second step

- I don't think that this should be an OOP project
  - I'm not a fan of Python OOP anyway it's a bit fucky imo.
- Plus the site provides a lot of different categories but right now the recipe endpoints should be fine.
- First one I would like to do is `search recipes by ingredients`, that would be the most logical thing to do
- Linux terminal image viewing support for terminal emulators that allow it

## Third step

- Possible GUI feature using: TKinter
- Docker containerized the whole project
  - Then create the jenkins pipeline for it to automate the task
  - (Thinking about private repository, would need a separate server for that, probably ghcr for now)
