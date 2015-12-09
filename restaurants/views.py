from django.shortcuts import render, Http404
import markdown
from .models import Restaurant, MenuItem
import random

import re

from django.db.models import Q

# Create your views here.
def all(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}
    template = 'restaurants/all.html'   
    return render(request, template, context)



def single(request, slug):
    user = request.user
    restaurant = Restaurant.objects.get(slug=slug)
    template = 'restaurants/single.html'
    menus = restaurant.menutitle_set.all()
    show_presentation_list = []

    for menu in menus:
        if menu.mealtype and menu.mealtype not in show_presentation_list:
            menu.show_presentation = True
            show_presentation_list.append(menu.mealtype)


    context = {
            'restaurant': restaurant,
            'menus': menus,
            'menu': menu,
    }
    return render(request, template, context)





def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


def search(request):
    quotes = [
        '"Life is uncertain. Eat dessert first" - Ernestine Ulmer', 
        '"There is no sincerer love than the love of food" - George Bernard Shaw', 
        '"All you need is love. But a little chocolate now and then doesn\'t hurt" - Charles M. Schulz', 
        '"If more of us valued food and cheer and song above hoarded gold, it would be a merrier world" - J.R.R. Tolkien',  
        '"One cannot think well, love well, sleep well, if one has not dined well." - Virginia Woolf',
        '"I love you like a fat kid loves cake!" - Scott Adams', 
        '"If you\'re afraid of butter, use cream" - Julia Child', 
        '"First we eat, then we do everything else" - M.F.K. Fisher', 
        '"Age and glasses of wine should never be counted" - Unknown', 
        '"In wine there is wisdom, in beer there is strength, in water there is bacteria" - David Auerbach', 
        '"Wine and cheese are ageless companions, like aspirin and aches, or June and moon, or good people and noble ventures" - M.F.K. Fisher', 
        '"You don\'t need a silver fork to eat good food" - Paul Prudhomme', 
        '"I have made a lot of mistakes falling in love, and regretted most of them, but never the potatoes that went with them" - Nora Ephron', 
        '"The only time to eat diet food is while you\'re waiting for the steak to cook" - Julia Child', 
        '"I cook with wine. Sometimes I even add it to the food" - W.C. Fields', 
        '"We all eat, and it would be a sad waste of opportunity to eat badly" - Anna Thomas',
        '"A balanced diet is a cookie in each hand" - Barbara Johnson', 
        '"People who love to eat are always the best people" - Julia Child', 
        '"My doctor told me I had to stop throwing intimate dinners for four unless there are three other people" - Orson Welles',  
        '"The secret of success in life is to eat what you like and let the food fight it out inside" - Mark Twain',
        '"It\'s difficult to think anything but pleasant thoughts while eating a homegrown tomato" - Lewis Grizzard', 
        '"My weaknesses have always been food and men -- in that order" - Dolly Parton', 
        '"Cooking is like love. It should be entered into with abandon or not at all" - Harriet van Horne',
        '"He was a bold man that first ate an oyster" - Jonathan Swift', 
        '"Food is symbolic of love when words are inadequate" - Alan D. Wolfelt', 
        '"Vegetables are a must on a diet. I suggest carrot cake, zucchini bread and pumpkin pie" - Jim Davis', 
        '"All happiness depends on a leisurely breakfast" - John Gunther',
        '"Human beings do not eat nutrients, they eat food" -  Mary Catherine Bateson', 
        '"All sorrows are less with bread" - Miguel de Cervantes', 
        '"I don\'t like food that\'s too carefully arranged; it makes me think that the chef is spending too much time arranging and not enough time cooking. If I wanted a picture I\'d buy a painting" - Andy Rooney', 
        '"Nothing would be more tiresome than eating and drinking if God had not made them a pleasure as well as a necessity" - Voltaire',
        '"As I ate the oysters with their strong taste of the sea and their faint metallic taste that the cold white wine washed away, leaving only the sea taste and the succulent texture, and as I drank their cold liquid from each shell and washed it down with the crisp taste of the wine, I lost the empty feeling and began to be happy and to make plans" - Ernest Hemingway', 
        '"One should eat to live, not live to eat" - Moliere', 
        '"When baking, follow directions. When cooking, go by your own taste" - Laiko Bahrs', 
        '"Tomatoes and oregano make it Italian; wine and tarragon make it French. Sour cream makes it Russian; lemon and cinnamon make it Greek. Soy sauce makes it Chinese; garlic makes it good" - Alice May Brock',
        '"A crust eaten in peace is better than a banquet partaken in anxiety" - Aesop', 
        '"I come from a family where gravy is considered a beverage" - Erma Bombeck', 
        '"So long as you have food in your mouth, you have solved all questions for the time being" - Franz Kafka',
        '"Spaghetti can be eaten most successfully if you inhale it like a vacuum cleaner" - Sofia Loren', 
        '"You can tell a lot about a fellow\'s character by his way of eating jellybeans" - Ronald Reagan',
        '"We may find in the long run that tinned food is a deadlier weapon than the machine gun" - George Orwell', 
        '"Salt is born of the purest of parents: the sun and the sea" - Pythagoras', 
        '"An empty belly is the best cook" - Estonian Proverb', 
        '"Did you ever stop to taste a carrot? Not just eat it, but taste it? You can\'t taste the beauty and energy of the earth in a Twinkie" - Astrid Alauda', 
        '"Life is a combination of magic and pasta" - Federico Fellini',
        '"Cheese - milk\'s leap toward immortality" - Clifton Fadiman', 
        '"My favorite time of day is to get up and eat leftovers from dinner, especially spicy food" - David Byrne', 
        '"Food should be fun" - Thomas Keller', 
        '"Tell me what you eat, and I will tell you what you are" - Anthelme Brillat Savarin', 
        '"If you wish to make an apple pie truly from scratch, you must first invent the universe" - Carl Sagan',
        '"One of the very nicest things about life is the way we must regularly stop whatever it is we are doing and devote our attention to eating" - Luciano Pavarotti', 
        '"The more you eat, the less flavor; the less you eat, the more flavor" - Chinese Proverb', 
        '"You could probably get through life without knowing how to roast a chicken, but the question is, would you want to?" - Nigella Lawson', 
        '"He who distinguishes the true savor of his food can never be a glutton; he who does not cannot be otherwise" - Henry David Thoreau', 
        '"Soup is just a way of screwing you out of a meal" - Jay Leno',
        '"Good bread is the most fundamentally satisfying of all foods; good bread with fresh butter, the greatest of feasts!" - James Beard', 
        '"Life is too short for self-hatred and celery sticks" - Marilyn Wann', 
        '"When the world wearies, and society ceases to satisfy, there is always the garden" - Minnie Aumonier', 
        '"A gourmet who thinks of calories is like a tart who looks at her watch" - James Beard', 
        '"A man may be a pessimistic determinist before lunch and an optimistic believer in the will\'s freedom after it" - Aldous Huxley',
        '"Probably one of the most private things in the world is an egg until it is broken" - MFK Fisher', 
        '"We are indeed much more than what we eat, but what we eat can nevertheless help us to be much more than what we are" - Adelle Davis', 
        '"When eating fruit, remember who planted the tree; when drinking water, remember who dug the well" - Vietnamese Proverb', 
        '"My favorite animal is steak" - Fran Lebowitz', 
        '"The poets have been mysteriously silent on the subject of cheese" - G.K. Chesterton',
        '"If there were only turnips and potatoes in the world, someone would complain that plants grow the wrong way" - Georg C. Lichtenberg', 
        '"A fruit is a vegetable with looks and money. Plus, if you let fruit rot, it turns into wine, something brussel sprouts never do" - P.J. O\'Rourke', 
        '"Lettuce is like conversation; it must be fresh and crisp, so sparkling that you scarcely notice the bitter in it" - Charles Dudley Warner',
        '"To me, life without veal stock, pork fat, sausage, organ meat, demi-glace, or even stinky cheese is a life not worth living" - Anthony Bourdain',
        '"I am prepared to believe that a dry martini slightly impairs the palate, but think what it does for the soul." - Alex Waugh', 
        '"Bread, milk and butter are of venerable antiquity. They taste of the morning of the world" - Leigh Hunt', 
        '"I will marry you if you promise not to make me eat eggplant" - Gabriel Garcia Marquez', 
        '"Only the pure in heart can make a good soup" - Ludwig van Beethoven', 
        '"When a man\'s stomach is full it makes no difference whether he is rich or poor" - Eurepides',
        '"The act of putting into your mouth what the earth has grown is perhaps your most direct interaction with the earth" - Frances Moore Lappe', 
        '"Cuisine is only about making foods taste the way they are supposed to taste" - Charlie Trotter', 
        '"Shake the hand that feeds you" - Michael Pollan', 
        '"The discovery of a new dish does more for the happiness of the human race than the discovery of a star" - Jean Anthelme Brillat-Savarin', 
        '"After a full belly all is poetry" - Frank McCourt',
        '"Food is symbolic of love when words are inadequate" - Alan D. Wolfelt', 
        '"Ask not what you can do for your country. Ask what\'s for lunch" - Orson Wells', 
        '"Cookery is not chemistry. It is an art. It requires instinct and taste rather than exact measurements" - Marcel Boulestin', 
        '"Cooking is so popular today because it\'s the perfect mix of food and fun" - Emeril Lagasse', 
        '"Secrets, especially with cooking, are best shared so that the cuisine lives on" - Bo Songvisava',
        '"Cooking is an observation-based process that you can\'t do if you\'re so completely focused on a recipe" - Alton Brown', 
        '"Cooking demands attention, patience, and above all, a respect for the gifts of the earth. It is a form of worship, a way of giving thanks" - Judith B. Jones', 
        '"Life itself is the proper binge" - Julia Child', 
        '"Never work before breakfast; if you have to work before breakfast, eat your breakfast first" - Josh Billings', 
        '"I don\'t cry over spilt milk, but a fallen scoop of ice cream is enough to ruin my whole day" - Terri Guillemets',
        '"There\'s nothing better than a good friend, except a good friend with chocolate" - Linda Grayson', 
        '"Wine and cheese are ageless companions, like aspirin and aches, or June and moon, or good people and noble ventures" - M.F.K. Fisher', 
        '"Plain fresh bread, its crust shatteringly crisp. Sweet cold butter. There is magic in the way they come together in your mouth to make a single perfect bite" - Ruth Reichl', 
        '"Remember that a very good sardine is always preferable to a not that good lobster" - Ferran Adria', 
        '"Water is the most neglected nutrient in your diet but one of the most vital" - Kelly Barton',
        '"There are many miracles in the world to be celebrated and, for me, garlic is the most deserving" - Leo Buscaglia', 
        '"He that but looketh on a plate of ham and eggs to lust after it hath already committed breakfast in his heart" - C. S. Lewis', 
        '"If food is poetry, is not poetry also food?" - Joyce Carol Oates',
        '"Popcorn for breakfast! Why not? It\'s a grain. It\'s like grits, but with high self-esteem" - James Patterson',
        '"Seize the moment. Remember all those women on the \'Titanic\' who waved off the dessert cart" - Erma Bombeck', 
        '"Don\'t wreck a sublime chocolate experience by feeling guilty. Chocolate isn\'t like premarital sex. It will not make you pregnant. And it always feels good" - Lora Brody', 
        '"Ice-cream is exquisite. What a pity it isn\'t illegal" - Voltaire', 
        '"Whoever thought a tiny candy bar should be called fun size was a moron" - Glenn Beck', 
        '"The odds of going to the store for a loaf of bread and coming out with only a loaf of bread are three billion to one" - rma Bombeck',
        '"After a good dinner one can forgive anybody, even one\'s own relations" - Oscar Wilde', 
        '"Pull up a chair. Take a taste. Come join us. Life is so endlessly delicious" - Ruth Reichl', 
        '"It\'s absolutely unfair for women to say that guys only want one thing: sex. We also want food" - Jarod Kintz', 
        '"Humor keeps us alive. Humor and food. Don\'t forget food. You can go a week without laughing" - Joss Whedon', 
        '"Am I tough? Am I strong? Am I hard-core? Absolutely. Did I whimper with pathetic delight when I sank my teeth into my hot fried-chicken sandwich? You betcha" - James Patterson',
        '"Let food be thy medicine and medicine be thy food" - Hippocrates', 
        '"What I say is that, if a man really likes potatoes, he must be a pretty decent sort of fellow" - A.A. Milne', 
        '"I wish my stove came with a Save As button like Word has. That way I could experiment with my cooking and not fear ruining my dinner" - Jarod Kintz', 
        '"We must have a pie. Stress cannot exist in the presence of a pie" - David Mamet', 
        '"I am not a glutton - I am an explorer of food" - Erma Bombeck',
        '"I am the broth of love. Make soup to me" - Jarod Kintz', 
        '"Anything is good if it\'s made of chocolate" - Jo Brand', 
        '"You better cut the pizza in four pieces because I\'m not hungry enough to eat six" - Yogi Berra', 
        '"Blood may be thicker than water, but it\'s certainly not as thick as ketchup. Nor does it go as well with French fries" - Jarod Kintz', 
        '"My love is pizza shaped. Won\'t you have a slice? It\'s circular, so there\'s enough to go around" - Dora J. Arod',
        '"Cooking is at once child\'s play and adult joy. And cooking done with care is an act of love" - Craig Claiborne', 
        '"The main facts in human life are five: birth, food, sleep, love and death" - E.M. Forster', 
        '"Don\'t let love interfere with your appetite. It never does with mine" - Anthony Trollope', 
        '"Sex is good, but not as good as fresh sweet corn" - Garrison Keillor', 
        '"No man is lonely while eating spaghetti: it requires so much attention" - Christopher Morley',
        '"Fools make feasts and wise men eat them" - Benjamin Franklin', 
        '"Fat gives things flavor" - Julia Child',
        '"Cakes are like books: There are new ones you want to read and old favorites you want to reread" - Ellen Rose',
        '"Somebody get me a cheeseburger!" - Steve Miller Band', 
        '"To eat well in England you should have breakfast three times a day" - W. Somerset Maugham', 
        '"Food, like a loving touch or a glimpse of divine power, has that ability to comfort" - Norman Kolpas', 
        '"Though their life was modest, they believed in eating well" - James Joyce', 
        '"The trouble with eating Italian is that 5 or 6 days later, you\'re hungry again" - George Miller',
        '"Hard work should be rewarded by good food" - Ken Follett', 
    ]

    query_string = ''
    found_entries = None
    quote = random.choice(quotes)

    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        #this entry query allows you enter multiple search terms for eg ['restaurant_name', 'restaurant_state',]
        # todo: maybe do the search function like allmenu. Search by state, then do another search by name, add, etc
        entry_query = get_query(query_string, ['restaurant_name', 'restaurant_state', 'restaurant_address1', 'restaurant_address2'])
        restaurants = Restaurant.objects.all()
        for restaurant in restaurants:
            restaurant_names = str(restaurant)
            restaurant_names_split = ''.join(restaurant_names.split())       

        found_entries = Restaurant.objects.filter(entry_query)
        if len(found_entries) == 0 or None:
            nothing_found = "Sorry no results"
            template = 'restaurants/results.html'
            context = {
                'query_string': query_string,
                'found_entries': found_entries,
                'quote': quote,
                'nothing_found': nothing_found,
            }
            return render(request, template, context)


    else:
        no_query = "Looks like you didn\'t type anything. Give it another try"
        template = 'restaurants/results.html'
        context = {
            'query_string': query_string,
            'found_entries': found_entries,
            'quote': quote,
            'no_query': no_query
        }
        return render(request, template, context)

    template = 'restaurants/results.html'
    context = {
        'query_string': query_string,
        'found_entries': found_entries,
        'quote': quote,
    }

    return render(request, template, context)




