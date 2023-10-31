presets_data = [
    {
      "name": "Product Feature to Benefit",
      "max_tokens": 200,
      "temperature": 0.4,
      "stop_sequences": [],
      "prompt": """Turn the following product feature into a list of benefits. Group them into three types of benefits: Functional Benefits, Emotional Benefits, and Social Benefits.

Product Feature:
Our app automatically transcribes your meetings. It uses state-of-the-art speech-to-text technology that works even in noisy backgrounds. Once the transcription is done, our app creates its summary and automatically emails it to the meeting attendees.""",
      "expected_output": """Functional Benefits:
- Save time by not having to manually transcribe your meetings
- Increase accuracy by not having to rely on human transcribers
- Reduce costs by not having to hire human transcribers 

Emotional Benefits:
- Reduce stress by not having to worry about transcribing your meetings
- Increase confidence by knowing that your meetings are being transcribed accurately
- Boost productivity by not having to spend time on transcribing your meetings 

Social Benefits:
- Encourage collaboration by sharing the meeting summary with the meeting attendees
- Improve communication by making sure that the meeting summary is accurate
- Increase transparency by providing a record of the meeting for everyone to see."""
    },
    {
      "name": "Product Pitch",
      "max_tokens": 200,
      "temperature": 0.5,
      "stop_sequences": [],
      "prompt": """Generate a pitch for the following product: An AI chess tutor

The pitch must include the following sections.
1. Problem
2. Solution
3. Features
4. Buyer Persona
5. Business Model

Problem:""",
      "expected_output": """Problem: Chess is a game of precision and strategy, but it can be difficult to improve your game without access to a trained coach or tutor. If you feel like you're stuck at a plateau and want to get better at chess, you deserve access to the best tools! 

Solution:
Introducing the world's first AI chess tutor! This app uses cutting-edge AI to provide you with the guidance and feedback you need to improve your game.

Features:

-Cutting-edge AI
-User-friendly interface
-Hundreds of exercises and puzzles
-Video tutorials from world-class coaches
-Chatbot for instant feedback

Buyer Persona:

People who are passionate about improving their chess game, especially:

-Beginners looking for a way to learn the basics
-Intermediate players who want to improve their game
-Advanced players looking for a way to hone their skills 

Business Model:

-Freemium"""
    },
    {
      "name": "Business Model Canvas",
      "max_tokens": 200,
      "temperature": 0.2,
      "stop_sequences": [],
      "prompt": """Generate a Business Model Canvas consisting of the following nine building blocks.
1 - Customer Segments
2 - Value Propositions
3 - Channels
4 - Customer Relationships
5 - Revenue Streams
6 - Key Resources
7 - Key Activities
8 - Key Partners
9 - Cost Structure

Business Model Canvas
Product: Satellite broadband service

1 - Customer Segments:""",
      "expected_output": """Residential customers, Small and medium-sized businesses, Large enterprises, Government and military institutions.

2 - Value Propositions:
Reliable and consistent internet connectivity, even in remote or rural areas.
Fast internet speeds ranging from 5 Mbps to 1 Gbps.
Affordable prices with flexible pricing plans.
Customer-centric support and service.

3 - Channels:
Satellite broadband service can be accessed through a satellite dish and modem, which can be purchased or rented from the service provider.
Marketing and advertising channels include online, print, and television advertising, as well as word-of-mouth referrals.

4 - Customer Relationships:
Long-term relationships with customers, with a focus on customer service and support.
Regularly communicate with customers to understand their needs and provide updates on service improvements.

5 - Revenue Streams:
Revenue is generated through monthly subscriptions for the satellite broadband service, with optional add-ons such as increased data usage or faster"""
    },
    {
      "name": "Email Keyword Extraction",
      "max_tokens": 40,
      "temperature": 0.4,
      "stop_sequences": ["--"],
      "prompt": """Extract the product and return address from this email:

Dear Elliott,

Unfortunately, your item, Supreme The North Face Statue of Liberty Baltoro Jacket, was not accepted for verification.
We will be shipping this back to 171 John Street, Toronto ON, M5T 1X2.

Product:""",
      "expected_output": """Supreme The North Face Statue of Liberty Baltoro Jacket
Return Address: 171 John Street, Toronto ON, M5T 1X2 
"""
    },
    {
      "name": "Simplify Technical Concepts",
      "max_tokens": 158,
      "temperature": 0,
      "stop_sequences": ["--"],
      "prompt": """Simplify the following technical explanation.

The core idea of information theory is that the informational value of a communicated message depends on the degree to which the content of the message is surprising. If a highly likely event occurs, the message carries very little information. On the other hand, if a highly unlikely event occurs, the message is much more informative.""",
      "expected_output": """Information theory is based on the idea that the more surprising an event is, the more information it carries."""
    },
    {
      "name": "Keywords To Email",
      "max_tokens": 150,
      "temperature": 0.2,
      "stop_sequences": ["--"],
      "prompt": """Write an email about the following:
- launch of new fitness watch series
- email or live chat for any questions.""",
      "expected_output": """Hello, 

We are excited to announce the launch of our new fitness watch series. We have been working hard to bring you the best watches possible and we are confident that you will love them.

If you have any questions about the new series, please don't hesitate to contact us via email or live chat. We will be more than happy to help.

Thank you,
[Your Name]""",
    },
    {
      "name": "Victorian Style Writing",
      "max_tokens": 420,
      "temperature": 0.7,
      "stop_sequences": [],
      "prompt": """Turn the following text into beautiful and wandering Victorian prose without changing the original meaning.

Original Text:
"He was average." 

Victorian prose: 
"He was, in the way of most men, possessed of a rudimentary intelligence, his countenance ordinary, his bearing mild, with some weakness about the shoulders, his hair the color of ash; he spoke of the weather."

Original Text:
"It's a good thing America got to the moon first." 

Victorian prose:
"It is a matter of singular wonder that America, being the chief seat of learning and the repository of all arts and sciences, made herself mistress of the heavens, and in so doing reached across the blackness of cosmos to touch the gleaming silver moon."

Original Text:
"I'm feeling ok" 
Victorian prose:""",
      "expected_output": "I am at peace, with the weight of the world removed from my shoulders, and with a clear mind, untroubled by the trivialities of life, I feel an untroubled joy, and an untroubled hope, for my future."
    }
]
