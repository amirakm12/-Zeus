# UMHH Super Sonic AI Agent – To-Do List Extension

Now includes a fully working to-do list skill with local storage using `todo_data.json`.

## Usage

- Add a to-do:  
  `"Add todo: Your task here"`
- List all to-dos:  
  `"List todos"`
- Mark a to-do as done:  
  `"Mark done 1"` (where 1 is the to-do id)
- Remove a to-do:  
  `"Remove todo 1"`

To test, simply run:

```
python main.py
```

You’ll see output for each to-do action.

## Where is the data stored?

All tasks are persisted in the file `todo_data.json` in your working directory.

---