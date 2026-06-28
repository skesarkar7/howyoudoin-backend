"""
Static emotion taxonomy: primary -> secondary -> [tertiary, tertiary].
This never changes at runtime, so it's served as a simple read-only endpoint
rather than being stored in the database.
"""

EMOTIONS = {
    "Bad": {
        "Bored": ["Indifferent", "Apathetic"],
        "Busy": ["Pressured", "Rushed"],
        "Stressed": ["Overwhelmed", "Out of control"],
        "Tired": ["Sleepy", "Unfocussed"]
    },
    "Fearful": {
        "Scared": ["Helpless", "Frightened"],
        "Anxious": ["Overwhelmed", "Worried"],
        "Insecure": ["Inadequate", "Inferior"],
        "Weak": ["Worthless", "Insignificant"],
        "Rejected": ["Excluded", "Persecuted"],
        "Threatened": ["Nervous", "Exposed"]
    },
    "Angry": {
        "Let down": ["Betrayed", "Resentful"],
        "Humiliated": ["Disrespected", "Ridiculed"],
        "Bitter": ["Indignant", "Violated"],
        "Mad": ["Furious", "Jealous"],
        "Aggressive": ["Provoked", "Hostile"],
        "Frustrated": ["Infuriated", "Annoyed"],
        "Distant": ["Withdrawn", "Numb"],
        "Critical": ["Sceptical", "Dismissive"]
    },
    "Disgusted": {
        "Disapproving": ["Judgmental", "Embarrassed"],
        "Disappointed": ["Appalled", "Revolted"],
        "Awful": ["Nauseated", "Detestable"],
        "Repelled": ["Horrified", "Hesitant"]
    },
    "Sad": {
        "Hurt": ["Embarrassed", "Disappointed"],
        "Depressed": ["Inferior", "Empty"],
        "Guilty": ["Remorseful", "Ashamed"],
        "Despair": ["Powerless", "Grief"],
        "Vulnerable": ["Fragile", "Victimised"],
        "Lonely": ["Abandoned", "Isolated"]
    },
    "Happy": {
        "Optimistic": ["Inspired", "Hopeful"],
        "Trusting": ["Intimate", "Sensitive"],
        "Peaceful": ["Thankful", "Loving"],
        "Powerful": ["Creative", "Courageous"],
        "Accepted": ["Valued", "Respected"],
        "Proud": ["Confident", "Successful"],
        "Interested": ["Inquisitive", "Curious"],
        "Content": ["Joyful", "Free"],
        "Playful": ["Cheeky", "Aroused"]
    },
    "Surprised": {
        "Excited": ["Energetic", "Eager"],
        "Amazed": ["Awe", "Astonished"],
        "Confused": ["Perplexed", "Disillusioned"],
        "Startled": ["Dismayed", "Shocked"]
    }
}

# One-line explanation per emotion name. Flat lookup by name rather than by
# tree position: a handful of names (Overwhelmed, Inferior, Embarrassed,
# Disappointed) appear under more than one branch, but their meaning is the
# same or close enough in both places that one description covers both.
EMOTION_DESCRIPTIONS = {
    # Bad
    "Bad": "A general sense that things aren't going well.",
    "Bored": "Feeling unstimulated and unable to find interest in what's happening.",
    "Indifferent": "Not caring much about the outcome or situation.",
    "Apathetic": "Lacking motivation, enthusiasm, or emotional investment.",
    "Busy": "Having many tasks competing for your attention.",
    "Pressured": "Feeling pushed to meet demands or expectations.",
    "Rushed": "Feeling there isn't enough time to do things properly.",
    "Stressed": "Feeling mentally or emotionally strained by demands.",
    "Overwhelmed": "Feeling that challenges or worries exceed your ability to cope.",
    "Out of control": "Feeling unable to influence or manage what's happening.",
    "Tired": "Lacking physical or mental energy.",
    "Sleepy": "Feeling the need to sleep.",
    "Unfocussed": "Finding it difficult to concentrate or stay attentive.",

    # Fearful
    "Fearful": "A general sense of fear or unease about something.",
    "Scared": "Feeling afraid of a perceived danger or threat.",
    "Helpless": "Feeling unable to change or improve the situation.",
    "Frightened": "Experiencing intense fear about something immediate.",
    "Anxious": "Feeling uneasy about uncertain future events.",
    "Worried": "Continuously thinking about possible negative outcomes.",
    "Insecure": "Doubting your own worth or abilities.",
    "Inadequate": "Feeling not good enough for what's expected.",
    "Inferior": "Feeling less capable or valuable than others.",
    "Weak": "Feeling physically or emotionally lacking strength.",
    "Worthless": "Feeling as though you have little or no value.",
    "Insignificant": "Feeling unimportant or unnoticed.",
    "Rejected": "Feeling unwanted or not accepted by others.",
    "Excluded": "Feeling left out of a group or activity.",
    "Persecuted": "Feeling unfairly targeted or treated.",
    "Threatened": "Feeling your safety, status, or wellbeing is at risk.",
    "Nervous": "Feeling uneasy before something uncertain or challenging.",
    "Exposed": "Feeling vulnerable because others can judge or harm you.",

    # Angry
    "Angry": "A general sense of anger or irritation.",
    "Let down": "Feeling disappointed because expectations weren't met.",
    "Betrayed": "Feeling hurt because someone broke your trust.",
    "Resentful": "Feeling lingering anger over unfair treatment.",
    "Humiliated": "Feeling deeply ashamed after being embarrassed publicly.",
    "Disrespected": "Feeling your dignity or opinions weren't valued.",
    "Ridiculed": "Feeling mocked or made fun of.",
    "Bitter": "Feeling persistent anger mixed with disappointment.",
    "Indignant": "Feeling angry because something seems unfair or unjust.",
    "Violated": "Feeling that your rights, boundaries, or trust were broken.",
    "Mad": "Feeling strongly angry or irritated.",
    "Furious": "Feeling extremely intense anger.",
    "Jealous": "Feeling upset because someone else has something you want.",
    "Aggressive": "Feeling inclined to confront or attack.",
    "Provoked": "Feeling anger triggered by someone's actions.",
    "Hostile": "Feeling openly unfriendly or antagonistic.",
    "Frustrated": "Feeling annoyed because progress is blocked.",
    "Infuriated": "Feeling extremely angry over a situation.",
    "Annoyed": "Feeling mildly irritated by something.",
    "Distant": "Feeling emotionally detached from others.",
    "Withdrawn": "Pulling away from people or interactions.",
    "Numb": "Feeling emotionally disconnected or unable to feel much.",
    "Critical": "Focusing on faults or problems.",
    "Sceptical": "Doubting the truth or value of something.",
    "Dismissive": "Rejecting something as unimportant without much consideration.",

    # Disgusted
    "Disgusted": "A general sense of disgust or revulsion.",
    "Disapproving": "Feeling something is wrong or unacceptable.",
    "Judgmental": "Forming harsh opinions about others.",
    "Embarrassed": "Feeling self-conscious after an awkward or uncomfortable situation.",
    "Disappointed": "Feeling sad or let down because reality didn't meet expectations.",
    "Appalled": "Feeling shocked by something morally wrong.",
    "Revolted": "Feeling intense disgust toward something.",
    "Awful": "Feeling extremely unpleasant or miserable.",
    "Nauseated": "Feeling sickened physically or emotionally.",
    "Detestable": "Feeling that something is deeply hateful or disgusting.",
    "Repelled": "Feeling a strong desire to avoid something unpleasant.",
    "Horrified": "Feeling shocked and disgusted by something terrible.",
    "Hesitant": "Feeling reluctant because something feels wrong or unsafe.",

    # Sad
    "Sad": "A general sense of sadness or low mood.",
    "Hurt": "Feeling emotional pain caused by someone's words or actions.",
    "Depressed": "Feeling persistently low, hopeless, or emotionally drained.",
    "Empty": "Feeling emotionally hollow or disconnected.",
    "Guilty": "Feeling responsible for doing something wrong.",
    "Remorseful": "Feeling deep regret and wishing you had acted differently.",
    "Ashamed": "Feeling bad about yourself rather than just your actions.",
    "Despair": "Feeling that there's no hope for improvement.",
    "Powerless": "Feeling unable to change the situation.",
    "Grief": "Deep sorrow caused by significant loss.",
    "Vulnerable": "Feeling emotionally exposed or easily hurt.",
    "Fragile": "Feeling emotionally delicate or easily broken.",
    "Victimised": "Feeling harmed or unfairly treated by others.",
    "Lonely": "Feeling a lack of meaningful connection with others.",
    "Abandoned": "Feeling left behind by someone important.",
    "Isolated": "Feeling cut off from people or support.",

    # Happy
    "Happy": "A general sense of happiness or wellbeing.",
    "Optimistic": "Expecting positive outcomes in the future.",
    "Inspired": "Feeling motivated by a new idea or example.",
    "Hopeful": "Believing that things can improve.",
    "Trusting": "Feeling confident that others have good intentions.",
    "Intimate": "Feeling emotionally close to someone.",
    "Sensitive": "Being open and emotionally responsive to others.",
    "Peaceful": "Feeling calm and free from inner conflict.",
    "Thankful": "Feeling grateful for what you have received.",
    "Loving": "Feeling deep care and affection for someone.",
    "Powerful": "Feeling capable of making things happen.",
    "Creative": "Feeling able to produce new ideas or solutions.",
    "Courageous": "Feeling ready to face fear despite risks.",
    "Accepted": "Feeling welcomed and appreciated by others.",
    "Valued": "Feeling that your contributions matter.",
    "Respected": "Feeling that others recognize your worth and dignity.",
    "Proud": "Feeling satisfied with your achievements or character.",
    "Confident": "Trusting your own abilities and judgment.",
    "Successful": "Feeling you've achieved an important goal.",
    "Interested": "Wanting to learn or know more.",
    "Inquisitive": "Actively asking questions to understand.",
    "Curious": "Feeling eager to explore or discover something.",
    "Content": "Feeling satisfied with how things are.",
    "Joyful": "Feeling intense happiness and delight.",
    "Free": "Feeling unrestricted and able to be yourself.",
    "Playful": "Feeling lighthearted and ready to have fun.",
    "Cheeky": "Being mischievous in a playful way.",
    "Aroused": "Feeling physically or emotionally excited or stimulated.",

    # Surprised
    "Surprised": "A general sense of surprise about something unexpected.",
    "Excited": "Feeling enthusiastic and energized about something.",
    "Energetic": "Feeling full of vitality and drive.",
    "Eager": "Looking forward to something with enthusiasm.",
    "Amazed": "Feeling astonishment at something remarkable.",
    "Awe": "Feeling wonder mixed with admiration or reverence.",
    "Astonished": "Feeling extremely surprised by something unexpected.",
    "Confused": "Feeling unable to understand what's happening.",
    "Perplexed": "Feeling puzzled by something difficult to explain.",
    "Disillusioned": "Losing beliefs after reality disappoints expectations.",
    "Startled": "Feeling sudden surprise due to an unexpected event.",
    "Dismayed": "Feeling distressed by an unpleasant surprise.",
    "Shocked": "Feeling emotionally overwhelmed by something unexpected or disturbing.",
}
