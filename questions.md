### 1. Discuss your strategy and decisions implementing the application. Please, considertime complexity, effort cost, technologies used and any other variable that you understand important on your development process.

```bash
R: 
    My strategy was to create an application quickly, but efficiently, showing the user what they are looking for effectively and without much complexity.

    I used Python together with Flask, as I can create an API in a matter of seconds. I utilized the Pandas library because it is a very powerful tool for data manipulation in a fast and lightweight manner, as I believe that the less time the client has to wait for the page to load with the data, the better. I could have used more robust languages for the front-end and done more to visually impress the client, but since I prioritized agility and ease, I used HTML with JavaScript and Jinja2 to display the information quickly, lightly, and easily for the user.

    The design was created to avoid confusing the client accessing it, keeping it as simple as possible so that they can focus on other things instead of figuring out how to get to a place to obtain the answer they need.
```

### 2. How would you change your solution to account forfuture columns that might be requested, such as “Bill Voted On Date” or“Co-Sponsors”?

```bash
R: I would modify the Pandas filter so that the new fields are not excluded and, quickly and simply, I would insert them into the HTML code using Jinja2.
```

### 3. How would you change your solution if instead ofreceiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?

```bash
R: If I continued with the same business rule, I would merge the lists of legislators or bills through the DataFrame so that they are in just one variable, and I would use the to_csv function from Pandas to generate the CSV of these lists. If I need to generate one separate from the other, I would use the command twice.
```

### 4. How long did you spend working on the assignment?

```bash
R: The time spent researching, coding, thinking, and testing the application to ensure that the task was completed in a way that addressed all the proposed requirements and questions of the challenge was a total of 8 hours of work over the course of 2 days.
```
