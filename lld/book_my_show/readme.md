### Topics


1. Requirements and Goals of the System
2. Use case diagram
3. Class diagram
4. Activity Diagram
5. Code
6. Concurrency



#### Requirements and Goals of the System

Our ticket booking service should meet the following requirements:

    1. It should be able to list the cities where affiliate cinemas are located.
    2. Each cinema can have multiple halls and each hall can run one movie show at a time.
    3. Each Movie will have multiple shows.
    4. Customers should be able to search movies by their title, language, genre, release date, and city name.
    5. Once the customer selects a movie, the service should display the cinemas running that movie and its available shows.
    6. The customer should be able to select a show at a particular cinema and book their tickets.
    7. The service should show the customer the seating arrangement of the cinema hall. The customer should be able to select multiple seats according to their preference.
    8. The customer should be able to distinguish between available seats and booked ones.
    9. The system should send notifications whenever there is a new movie, as well as when a booking is made or canceled.
    10. Customers of our system should be able to pay with credit cards or cash.
    11. The system should ensure that no two customers can reserve the same seat.
    12. Customers should be able to add a discount coupon to their payment.
    
    
#### Use case diagram
We have five main Actors in our system:
    
    1. Admin
    2. FrontDeskOffice
    3. Customer
    4. Guest
    5. System
   
Here are the top use cases of the Movie Ticket Booking System:

    1. Search movies
    2. Create/Modify/View booking
    3. Make payment for booking
    4. Add a coupon to the payment
    5. Assign Seat
    6. Refund payment
    
