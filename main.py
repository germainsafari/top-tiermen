# app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    individuals = [

        {
            'name': "Iman Gadzhi",
            'profession': 'Entrepreneur',
            'net_worth': '$60 million',
            'books': ["Atomic Habits by James Clear",
                      "The Way of the Superior Man by David Deida",
                      "Meditations by Marcus Aurelius"],
            "Social Media": {
                "Twitter": "https://twitter.com/GadzhiIman",
                "YouTube": "https://www.youtube.com/c/ImanGadzhi",
                "Instagram": "https://www.instagram.com/imangadzhi"
            },
            "Image": "iman.jpg",
        },
        {
            'name': 'Steven Bartlett',
            'profession': 'Entrepreneur, speaker, investor, author, podcaster and BBC Dragon',
            'net_worth': '$600 million',
            'books': ['Happy Sexy Millionaire: Unexpected Truths about Fulfilment, Love and Success'],
            'twitter': 'https://twitter.com/stevebartlettsc',
            'youtube': 'https://www.youtube.com/c/StevenBartlett',
            'instagram': 'https://www.instagram.com/steven',
            'image': 'steven.jpg'
        },
        {
            'name': 'Tate Brothers',
            'profession': 'Entrepreneurs',
            'net_worth': '$400 million',
            'books': {
                'The Rational Male': 'Rollo Tomassi',
                'The 48 Laws of Power': 'Robert Greene',
                'The Millionaire Fastlane': 'M. J. DeMarco',
                'Atomic Habits': 'James Clear',
                'Think and Grow Rich': 'Napoleon Hill'
            },
            # Book 1 - The Rational Male by Rollo Tomassi. ...
            # Book 2 - The 48 Laws of Power by Robert Greene. ...
            # Book 3 - The Millionaire Fastlane by M. J. DeMarco. ...
            # Book 4 - Atomic Habits by James Clear. ...
            # Book 5 - Think and Grow Rich by Napoleon Hill.
            'twitter': 'https://twitter.com/Cobratate',
            'youtube': 'https://www.youtube.com/bsn',
            'instagram': 'https://www.instagram.com/tate_brothers',
            'image': 'tate.jpg'
        },
        {
            'name': 'Luke Belmar',
            'profession': 'Internet personality, investor, and entrepreneur',
            'net_worth': 'Unknown',
            'books': {
                'Time is Money': 'Aiden Nolan',
                'Scientific Advertising': 'Claude C. Hopkins',
                'The Art of War': 'Sun Tzu',
                'The Millionaire Master Plan': 'Roger James Hamilton',
                'The Changing World Order': 'Ray Dalio',
                'Shop Management': 'Frederick Winslow Taylor',
                'High Output Management': 'Andrew S. Grove',
                'Your Next Five Moves': 'Patrick Bet-David',
                'The 5 Levels of Leadership': 'John Maxwell',
                'The Lords of Easy Money': 'Cristopher Leonard',
                'Bitcoin: A Peer to Peer Electronic Cash System': 'Satoshi Nakamoto'
            },
            'twitter': 'https://twitter.com/lukebelmar',
            'youtube': 'https://www.youtube.com/@LukeBelmarVlogs',
            'instagram': 'https://www.instagram.com/lukebelmar',
            'image': 'luke.jpg'
        },
        {
            "Name": "Iman Gadzhi",
            "Profession": "Entrepreneur and digital marketer",
            "Net worth": "Estimated at $50 million",
            "Books": [
                "Atomic Habits by James Clear",
                "The Way of the Superior Man by David Deida",
                "Meditations by Marcus Aurelius"
            ],
            "Social Media": {
                "Twitter": "https://twitter.com/GadzhiIman",
                "YouTube": "https://www.youtube.com/c/ImanGadzhi",
                "Instagram": "https://www.instagram.com/imangadzhi"
            },
            "Image": "iman.jpg"
        },
        {
            'name': 'Umar Ashraf',
            'profession': 'Stock trader, entrepreneur, and coach',
            'net_worth': '20 millions',
            'books': ['None'],
            'twitter': 'https://twitter.com/umarashraf',
            'youtube': 'https://www.youtube.com/channel/UCir8ZEhgIOLY__2tN1Pi0ig',
            'instagram': 'https://www.instagram.com/umarashraf',
            'image': 'umar.png'
        },
        {
            'name': 'Bedros Keuilian',
            'profession': 'Entrepreneur, investor, coach, fitness expert, speaker, author, and influencer',
            'net_worth': '$200 millions',
            'books': ['Man Up: How to Cut the Bullshit and Kick Ass in Business (and in Life)'],
            'twitter': 'https://twitter.com/bedroskeuilian',
            'youtube': 'https://www.youtube.com/c/BedrosKeuilian',
            'instagram': 'https://www.instagram.com/bedroskeuilian',
            'image': 'bedros.jpg'
        },
        {
            'name': 'Patrick Bet David',
            'profession': 'Entrepreneur, author, and podcast host',
            'net_worth': '$500 millions',
            'books': ['Your Next Five Moves: Master the Art of Business Strategy',
                      'Doing The Impossible: The 25 Laws for Doing The Impossible'],
            'twitter': 'https://twitter.com/patrickbetdavid',
            'youtube': 'https://www.youtube.com/c/valuetainment',
            'instagram': 'https://www.instagram.com/patrickbetdavid',
            'image': 'patrick.jpg'
        },
        {
            'name': 'Codie Sanchez',
            'profession': 'Investor, writer, and venture capitalist',
            'net_worth': '$50 millions',
            'books': ['None'],
            'twitter': 'https://twitter.com/Codie_Sanchez',
            'youtube': 'https://www.youtube.com/c/CodieSanchez',
            'instagram': 'https://www.instagram.com/codiesanchez',
            'image': 'codie.jpg'
        },
        {
            'name': 'Jordan Welch',
            'profession': 'Entrepreneur, YouTuber, and dropshipper',
            'net_worth': '$20 million',
            'books': ['None'],
            'twitter': 'Unknown',
            'youtube': 'https://www.youtube.com/c/JordanWelch',
            'instagram': 'https://www.instagram.com/jordanwelch',
            'image': 'jordanwelch.jpg'
        },
        {
            'name': 'Michael Thurston',
            'profession': 'Personal trainer, fitness guru, and entrepreneur',
            'net_worth': 'Unknown',
            'books': ['None'],
            'twitter': 'https://twitter.com/thethurstonator',
            'youtube': 'https://www.youtube.com/c/MikeThurston',
            'instagram': 'https://www.instagram.com/mikethurston',
            'image': 'michealthurston.jpg'
        },

        {
            'name': 'michael huddleston',
            'profession': 'Investor, Fx trader',
            'net_worth': 'unknown',
            # 'books': ['Book 1', 'Book 2'],
            'twitter': 'https://twitter.com/I_Am_The_ICT',
            'youtube': 'https://www.youtube.com/@InnerCircleTrader',
            # 'instagram': 'https://www.instagram.com/tate_brothers',
            'image': 'michealh.jpg'
        },
        {
            'name': 'Dan Lok',
            'profession': 'Entrepreneur, author, speaker, podcaster, and venture capitalist',
            'net_worth': 'Unknown',
            'books': [
                'F.U. Money: Make As Much Money As You Damn Well Want And Live Your Life As You Damn Well Please!',
                'Influence!: 47 Forbidden Psychological Tactics You Can Use To Motivate, Influence and Persuade Your Prospect',
                'Unlock It: The Master Key to Wealth, Success, and Significance'
            ],
            'twitter': 'https://twitter.com/danthemanlok',
            'youtube': 'https://www.youtube.com/c/DanLok',
            'instagram': 'https://www.instagram.com/danlok',
            'image': 'danlok.jpg'
        },
        {
            'name': 'Jim Rohn',
            'profession': 'Motivational speaker, author, entrepreneur, and business coach',
            'net_worth': '$500 million by the time he died',
            'books': [
                'The Art of Exceptional Living',
                'The Seasons of Life',
                '7 Strategies for Wealth & Happiness',
                'The Power of Ambition'
            ],
            'youtube': 'Uhttps://www.youtube.com/watch?v=SKHopggBYAw',
            'image': 'jimrohn.jpg'
        },
        {
            'name': 'Kobe Bryant',
            'profession': 'Professional basketball player',
            'net_worth': '$600 million',  # estimated at the time of his death
            'books': [
                'The Mamba Mentality: How I Play',
                'Legacy and the Queen',
                'Geese Are Never Swans'
            ],
            'twitter': 'https://twitter.com/kobebryant',
            'instagram': 'https://www.instagram.com/kobebryant',
            'image': 'kobebryant.jpg'  # placeholder for actual path
        },
        {
            'name': 'Jose Zuniga',
            'profession': 'Entrepreneur, YouTube content creator',
            'channel': 'Teaching Men’s Fashion',
            'net_worth': 'Unknown',  # this data is often private
            'books': [],
            # as of my last training cut-off in September 2021, Jose Zuniga didn't have any published books
            'twitter': 'https://twitter.com/TMFmag',
            'youtube': 'https://www.youtube.com/user/Teachingmensfashion',
            'instagram': 'https://www.instagram.com/teachingmensfashion',
            'image': 'josezuniga.jpg'  # placeholder for actual path
        },
        {
            'name': 'Hamza Ahmed',
            'profession': 'YouTuber, fitness coach, and self-help guru',
            'net_worth': 'Unknown',  # this data is often private
            'books': [],
            # as of my last training cut-off in September 2021, Hamza Ahmed didn't have any published books
            'twitter': 'https://twitter.com/hamza97ahmed',
            'youtube': 'https://www.youtube.com/c/Hamza97',
            'instagram': 'https://www.instagram.com/hamza97ahmed',
            'image': 'hamzaahmed.jpg'  # placeholder for actual path
        }
        # Add information for other individuals here
    ]
    return render_template('index.html', individuals=individuals)


if __name__ == '__main__':
    app.run(debug=True)
