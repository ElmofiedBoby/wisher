GOAL: Wish list social media platform

Ever wondered what your friends want for the holidays/their birthday? Ever WISH there was an easy way to coordinate for big gifts? Wisher is the way.

PLAN:
1) Finish Backend (Python)
2) Finish CLI (Python or C)
3) Publish MVP
4) Dockerize
5) Finish Frontend (React)
6) Publish first release
67) Rewrite backend in C

ARCHITECTURE:

    User Class
        - Unique Float ID
        - Username
        - Password
        - Wishlist (array of items)
        - Claims (array of items references)
        
    Item Class
        - Name
        - Owner
        - Type
        - Link
        - Cost
        - Is claimed?
        - Claimed by (not visible to owner)
