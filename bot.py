import os, pickle, datetime, random

from models.user import User
from pathlib import Path
from twitchio.ext import commands, routines

TOKEN = os.environ['TMI_TOKEN']
CHANNELS = ['purpellvt']
MODERATORS = ['purpellvt', 'purpsybot']
USERDATAPATH = "userdata.txt"


class Bot(commands.Bot):

    userdata = None

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=TOKEN, prefix='!!', initial_channels=CHANNELS)
        userdata_path = Path(USERDATAPATH)
        userdata_path.touch()
        try:
            self.userdata=pickle.load(open(USERDATAPATH,"rb"))
        except EOFError:
            self.userdata = {}

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')


    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f'Hii hiiiii~ {ctx.author.name}!')


    @commands.command()
    async def d20(self, ctx: commands.Context):
        #Throws a D20 dice
        await ctx.send(f'You got {random.randint(1,20)}, {ctx.author.name}!')
    

    @commands.command()
    async def d6(self, ctx: commands.Context):
        #Throws a D6 dice
        await ctx.send(f'You got {random.randint(1,6)}, @{ctx.author.name}!')


    @commands.command()
    async def lurk(self, ctx: commands.Context):
        await ctx.send(f"Happy lurking @{ctx.author.name}! Don't forget to mute tab!")
        
        if self.userdata.get(ctx.author.name, None) is not None:
            self.userdata[ctx.author.name].set_lurktime(time=datetime.now())
        else:
            self.userdata[ctx.author.name] = User(0,datetime.now(),0)


    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command()
    async def unlurk(self, ctx: commands.Context):
        
        user = self.userdata.get(ctx.author.name)
        
        if user.get_lurktime() is None:
            await ctx.send(f"Welcome back @{ctx.author.name}!")
            return
        
        result = datetime.now() - user.get_lurktime()
        user.add_lurk(result)
        self.userdata[ctx.author.name]=user
        await ctx.send(f"Welcome back @{ctx.author.name}! Have been lurking for {int(result.total_seconds()//60)} minutes and {int(result.total_seconds()%60)} seconds.")
      
    @commands.cooldown(rate=1, per=43200, bucket=commands.Bucket.user)
    @commands.command()
    async def tarot(self, ctx: commands.Context):
        
        reverse: bool = random.choice([True, False])
        card: int = random.randint(0,21)
        
        await ctx.send('Shuffling cards...')

        match card:

            case 0:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Fool" reversed! 
                                   Keywords: reckless, careless, distracted, naive, foolish, gullible, stale, dull')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Fool" upright! 
                                   Keywords: beginnings, freedom, innocence, originality, adventure, idealism, spontaneity')
            
            case 1:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Magician" reversed! 
                                   Keywords: manipulation, cunning, trickery, wasted talent, illusion, deception')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Magician" upright! 
                                   Keywords: willpower, desire, being resourceful,, skill, ability, concentration, manifestation')
            
            case 2:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The High Priestess" reversed! 
                                   Keywords: repressed intuition, hidden motives, superficiality, confusion, cognitive dissonance')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The High Priestess" upright! 
                                   Keywords: unconscious, intuition, mystery, spirituality, higher power, inner voice')
            
            case 3:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Empress" reversed! 
                                   Keywords: insecurity, overbearing, negligence, smothering, lack of growth, lack of progress')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Empress" upright! 
                                   Keywords: divine feminine, sensuality, fertility, nurturing, creativity, beauty, abundance, nature')

            case 4:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Emperor" reversed! 
                                   Keywords: tyrant, domineering, rigid, stubborn, lack of discipline, recklessness')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Emperor" upright! 
                                   Keywords: stability, structure, protection, authority, control, practicality, focus, discipline')
            
            case 5:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Hierophant" reversed! 
                                   Keywords: rebellion, unconventionality, non-conformity, new methods, ignorance')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Hierophant" upright! 
                                   Keywords: tradition, social groups, conventionality, conformity, education, knowledge, beliefs')

            case 6:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Lovers" reversed! 
                                   Keywords: disharmony, imbalance, conflict, detachment, bad choices, indecision')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Lovers" upright! 
                                   Keywords: love, unions, partnerships, relationships, choices, romance, balance, unity')

            case 7:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Chariot" reversed! 
                                   Keywords: forceful, no direction, no control, powerless, aggression, obstacles')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Chariot" upright! 
                                   Keywords: success, ambition, determination, willpower, control, self-discipline, focus')

            case 8:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "Strength" reversed! 
                                   Keywords:  self-doubt, weakness, low confidence, inadequacy, cowardice, forcefulness')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "Strength" upright! 
                                   Keywords: courage, bravery, confidence, compassion, self-confidence, inner power')

            case 9:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Hermit" reversed! 
                                   Keywords: loneliness, isolation, recluse, being anti-social, rejection, returning to society')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Hermit" upright! 
                                   Keywords: self-reflection, introspection, contemplation, withdrawal, solitude, search for self')

            case 10:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Wheel of Fortune" reversed! 
                                   Keywords: bad luck, lack of control, clinging to control, unwelcome changes, delays')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Wheel of Fortune" upright! 
                                   Keywords: change, cycles, fate, decisive moments, luck, fortune, unexpected events')

            case 11:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "Justice" reversed! 
                                   Keywords: injustice, retribution, dishonesty, corruption, dishonesty, unfairness, avoiding accountability')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "Justice" upright! 
                                   Keywords: justice, karma, consequence, accountability, law, truth, honesty, integrity, cause and effect')

            case 12:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Hanged Man" reversed! 
                                   Keywords: stalling, disinterest, stagnation, avoiding sacrifice, standstill, apathy')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Hanged Man" upright! 
                                   Keywords: sacrifice, waiting, uncertainty, lack of direction, perspective, contemplation')

            case 13:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "Death" reversed! 
                                   Keywords: fear of change, repeating negative patterns, resisting change, stagnancy, decay')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "Death" upright! 
                                   Keywords: transformation, endings, change, transition, letting go, release')

            case 14:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "Temperance" reversed! 
                                   Keywords: imbalance, excess, extremes, discord, recklessness, hastiness')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "Temperance" upright! 
                                   Keywords: balance, peace, patience, moderation, calm, tranquillity, harmony, serenity')

            case 15:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Devil" reversed! 
                                   Keywords: independence, freedom, revelation, release, reclaiming power, reclaiming control')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Devil" upright! 
                                   Keywords: oppression, addiction, obsession, dependency, excess, powerlessness, limitations')

            case 16:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Tower" reversed! 
                                   Keywords: averting disaster, delaying the inevitable, resisting change')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Tower" upright! 
                                   Keywords: disaster, destruction, upheaval, trauma, sudden change, chaos')
            
            case 17:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Star" reversed! 
                                   Keywords: hopelessness, despair, negativity, lack of faith, despondent')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Star" upright! 
                                   Keywords: hope, inspiration, positivity, faith, renewal, healing, rejuvenation')
            
            case 18:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Moon" reversed! 
                                   Keywords: fear, deception, anxiety, misunderstanding, misinterpretation, clarity, understanding')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Moon" upright! 
                                   Keywords: illusion, intuition, uncertainty, confusion, complexity, secrets, unconscious')

            case 19:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Sun" reversed! 
                                   Keywords: blocked happiness, excessive enthusiasm, pessimism, unrealistic expectations, conceitedness')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The Sun" upright! 
                                   Keywords: happiness, success, optimism, vitality, joy, confidence, happiness, truth')

            case 20:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "Judgement" reversed! 
                                   Keywords: self-doubt, lack of self-awareness, failure to learn lessons, self-loathing')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "Judgement" upright! 
                                   Keywords: self-evaluation, awakening, renewal, purpose, reflection, reckoning')

            case 21:
                if reverse == True:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The World" reversed! 
                                   Keywords: lack of closure, lack of achievement, feeling incomplete, emptiness')
                else:
                    await ctx.send(f'{ctx.author.name} Your card of the day is "The World" upright! 
                                   Keywords: completion, achievement, fulfilment, sense of belonging, wholeness, harmony')
            
            case _:
                print("Something went wrong!")



bot = Bot()
bot.run()