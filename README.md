# VentureHub

## About

VentureHub is a web application to learn about up-and-coming startups that are bound to become the next "unicorns" of world.

## Technologies Used

VentureHub is mainly a Python application built on the Django framework. On the front-end, we've incorporated CSS and some light Javascript, as well as the Bootstrap framework to speed up the formatting. We also incorporated Material Design principles by Google to make the styling look more modern. On the back-end, we are using a SQLite database to store user and startup information.

In addition, we've included some third-party apps and libraries to give our project additional functionality. In terms of third-party apps, we've included the Upvote app, Registration-redux, and Crispy Forms. For some of the data science and analytics components, we've used Pandas, Matplotlib, and Sklearn.

### Functionality

We created several applications to piece together this project. The central application is the 'startups' app. This is a standard CRUD application that allows users to create a new startup and save it to the database, view the startups created, update the startups, and delete any startups from the database.

Additionally, we are using the Crunchbase API and the pycrunchbase library to extract key information on each startup created by a user. The API is called each time a startup's detail page is opened, rendering information regarding the company's description, the founders, key investors, and recent funding history. If a startup is not handled by the Crunchbase API, then a default page is shown for that startup.

The second application we created was the 'studio' app. This essentially calls the Soundcloud API to request a randomized podcast related to the subject of venture capital, technology, and entrepreneurship. Our hope is that the user will find this curated selection of podcasts a useful source of information.

The last application we created was the 'analytics' app. Here we scraped the Crunchbase database to look for broad trends in the startup and technology ecosystems. The first dataframe in the page looks at the evolution of venture funding from multiple phases (seed through H rounds) during the last 15 years. The recent uptick is useful to contextualize whether the current market is truly out of whack. The second dataframe basically looks at a "success rate" proxy by dividing the total number of exits (whether announced acquisitions or IPO) by the total number of investments in the database. We acknowledge that this is a rough estimate of success, but we think that it is directionally correct and an insightful look at over/under-rated venture funds.

Lastly, the home page is a simple landing-page with user registration and login. A user must register and login in order to access the apps main functionality.

## Team Homebrew

- Gustave Macheras
- Gurpratap Thiara
- Deb Bhadra
- Roger Teran
