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
