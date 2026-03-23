# NPC Dialogue Concepts & Overview

This document will go over how NPC dialogue and relationships should work.  
This code and these concepts will be open and available for anyone to use - just like... credit me pls n thx :3

## Initial Interaction

When first meeting an NPC, their opinion of you will likely be nothing. They may have heard of you if you have a local reputation and the NPC is more inclined to gossip, but by default they will not know you, naturally. This will be reflected in the code by all of their player relationship variables set to zero. They will have an introduction that will be largely based on their personality ([see also](#npc-dialogue-in-altering-players-personality)). *(Examples will reference Personalities from my Pokémon fan-project* [Pokémon GODOT](https://github.com/cami-camilleon))

**Examples:**  

> "Hey hey, I don't think I've seen you around before! The name's Calvin, but my friends call me Cal! What's your deal?"
> - a *Haphazard* NPC

> "Oh.. Um, were you looking at me?" [player response]
> - a *Soft* NPC; an example of a character introduction that might require a certain response to become aquainted with you.

> "Hey, you're the girl who helped out Fae, aren't you? What's your name?"
> - example of an NPC introduction given positive local reputation, citing a nonspecific example of a good deed.  

---  
  
**Note on local reputation:**
NPC's will have a list of other people they know. NPC's can know other characters in their own town or from out of town, and can have different levels of closeness with other NPC's. These factors will play into the weight of "repuation" for any given NPC.  
  
Some examples of this behavior:
> If Calvin is good friends with Fae, and your character does something to help Fae out, Calvin will have likely heard of this good deed, and have a positive opinion of you by the time you first talk to him. 
> - *Potentially, Calvin could even recognize you in town and approach you! "Hey! I'm friends with Fae and heard that you helped them out. That was cool of you. What was your name? Maybe I could ask you to help me out too?"*

> If Sayuri is partners with Natsumi, and you did something wrong by Natsumi, Sayuri will have a significanly negative opinion of you by the time you first talk to her. 
> - The closeness of the character you interacted with previously to the NPC will affect how swayed they are by local reputation. *"Aren't you that dude who hurt Sara's feelings? Yea, don't even talk to me." "Leave me alone."*

> If Arlo hates Marley, and you did something wrong by Marley, Arlo might have a slightly positive opinion of you by the time you first talk to him, depending on his personality. 
> - *Haphazard* NPCs will be more inclined to want to do wrong by other characters. Arlo might ask you to do more nefarious quests for him. *"Hey, whaddya say we get another one over on Marley, huh?" [yes/no] "Yeah, well let me know if you change your mind..."*

## Conversation Loop

Once you're personally acquainted with an NPC, each time you interact with them will yeild one of a few results:

- Most likely, the NPC will engage in one-sided small talk- just saying something about their day, something they're interested in, something about the world, etc. They may then prompt you to ask them what you need from them *("I'm yammering again- what did you need?")*. If not, see the next bullet.
    - If you've had this interaction with an NPC already, they will instead only prompt you to ask them what you need *("What's up?")*, giving you the opportunity to interact with them, which can include asking them their opinions on topics, asking their opinion on other NPCs you're acquainted with or met recently, giving them gifts, playing short games with them or doing [activities](#npc-activities) with them.
- The NPC may engage in two-sided small talk- they will ask you your opinion on something, whether you like a certain topic or in-game item for example, how you feel about another NPC, they may ask you to play a short game with them (a la rock paper scissors), or do an [activity](#npc-activities) with them, etc. This will be a good way to befriend NPCs. 
    - As you get closer to NPCs, you may be given non-explicit choices that can branch your relationship with them. This most often will be the option to romance NPCs. You can also unlock close-friend dialogue options once you are close enough with an NPC.
- The NPC may ask you to do a quest for them. This is another way to boost opinion of yourself. 

## NPC Activities

Doing activities with NPCs is going to be the most engaging way to interact with and strengthen and branch friendships with NPCs.  
Activities are going to take the form of cutscene-heavy minigames that you play with other characters. At the most simple, they will simply be cutscenes depicting your character doing an activity with an NPC, and at the most complicated, they will include perhaps quick-time events or decisions to make during the activity that may or may not impact the result of the activity.  
Activities will result in a change in an NPC's player relationship variables; in other words, a successful activity with a friend NPC will increase your friendship level by some amount, and an unsuccessful event (provided an event is multi-outcome) could damage your friendship with an NPC.  
Here are some examples of NPC activities:

> You and Mel are somewhat good friends, and decide to go shopping for clothes and accessories together. You may have to help them pick out clothes that seem to be more their style than others, and if successful, you can get more of a boost to your friendship. 
> - Failing a choice like this should be realistically low-consequence- an activity like this should usually always result in an increase of frienship level. Consider choices in activities like these to be opportunities to get extra boost to your friendship with an NPC. *"Which dress do you think suits me more, do you think?" [choice] "Really, you think so? I'll think about it, I guess... Thanks for your help."*

> You and Dmitri are close friends who might have feelings for each other (you have at least admitted to yourself that you have a crush on him. See *[Self-Dialogue](#self-dialogue)* for details on that mechanic.) You both decide to go get lunch and eat together at a local park. You may experience intermittent dialogue options between you and him where you can choose to either be more dry or be more flirty. 
> - This can work to branch your relationship and unlock more opportunities to romance Dmitri, if you would like to. *"This day is so nice- the lighting I think really makes your eyes pop, Player." [choice: "Aw, thats nice, thanks!" / "Wow you really think so? I was just thinking the same thing about your eyes..~"]* The choice to reciprocate flirtation will typically be the choices activities like this present.

## Self-Dialogue

Sometimes, you may be prompted (or yourself prompt) an introspection for your character. These act as opportunities to tell the game how you feel about things, other characters, etc. Rather than listen and answer to a narrator, these choices will present themselves as your own thoughts. In the case of progressing through a romance arc with an NPC, for example, your character might get a thought bubble above their head that you can interact with, which will invoke a self-dialogue prompting you to tell the game explicitly if you're romantically interested in an NPC that you may have hinted to the game that you might be.

> **Example: Romance Self-Dialogue**  
> Once you become close enough to an NPC, the game can begin throwing you dialogue options that would hint to them (and the game!) that you would like to try romancing them, if chosen.  
> 
> - *NPC: "Maybe next time we can hang out for even longer!" [choices: "Yeah, maybe! See you later." (generic) / "Yeah, that would be wonderful, I'd love that~" (romance hint) / "Meh, maybe not. That was enough socializing for one sitting lmao." (rude option)]*
> --- 
> Selecting the romance hint as your response will prompt the game at some point following this interaction to initiate a self-dialogue asking you if you have feelings for the NPC. You will see a thought bubble appear for a moment over your characters head, which upon clicking will trigger a dialogue with yourself:
> - *"Hmmm... I think... I might have... Do I have feelings for NPC... ??"  
    [choices: "No, no that's silly!" (denial) / "I... think I might... !!" (acceptance) / "No, certainly not." (certain denial)]*
>   - Denial: If you choose the soft denial option, the game will dismiss the self-dialogue but nothing internally will change regarding your relationship with the NPC. You will be prompted with another romance hint in a future interaction with them, which if you choose, it will prompt another self-dialogue which will be the same as this example, except without the option to soft denial. You make up your mind this time.
>   - Acceptance: This one is the most self-explanatory. If you accept the romance self-dialogue, the game would flag that you're romantically interested in the NPC in question, and interaction options would become available, including confessing your feelings in certain situations.
>   - Certain Denial: If you aren't interested in romancing a character- perhaps if you chose a romance hint by accident or as a gag- you can choose a certain denial in this self-dialogue. This would prompt a confirmation: *("Yeah, there's no chance I feel this way... right?" [prompt "Right." / "Well..."])* and if confirmed, the game will not prompt any romance hints or dialogue options for you to choose after this. The NPC could still potentially be romantically interested in you, which they may or may not prompt you about at some point even after denying it to yourself.  

NPC Romance confirmation would likely be the highest use case of self-dialogue, but some other uses of the mechanic could be:  
- Pondering if you should still be friends with an NPC or if you should ignore them or become enemies with them. 
- ***author note: uhmmm i'll think of some more uses and put them here idk LMAO***  

Self-dialogue could also be one-sided, as a means for the game to tell you things about yourself, as seen in [NPC Dialogue in Altering Player's Personality](#npc-dialogue-in-altering-players-personality)

### In short: NPC Interactions and Activities will change relationship values between your character and an NPC, and Self-Dialogues will basically confirm a change in relationship dynamic if needed. 

A self-dialogue will not always be necessary to branch a relationship- sometimes decisions can be made by the game based solely on the values present between you and an NPC. Self-dialogues are to be used when a player should be able to choose a branch for a relationship.  
For example, if you are rude to an NPC enough times, they can autonomously decide not to be your friend anymore. You can still be prompted to self-dialogue decide if you still want to be their friend or not, but that won't force your character and that NPC into a friendship. Much like real life, how the NPC percieves your character has just as much bearing on your relationship as how your character percieves them in the code.

## NPC Dialogue in Altering Player's Personality

When a player starts the game, they will get to choose an option for their character's personality. This chosen personality may or may not affect what options are avaliable when interacting with NPCs. It will certainly have a bearing on how friendly an NPC is with you (or perhaps more accurately, how easily friendable or romanceable an NPC is for you given your character's personality). What you choose at the beginning of the game will be the baseline for what the game sees your character's personality to be, but how you interact with NPCs will be able to fluctuate and change this.  
  
Again referencing the Personalities from Pokémon GODOT, let's say for example you choose *Soft* as your character's personality. This, again, may or may not give you dialogue options unique to that personality *(jury is still out on how feasible that would be to program...)*, however in any case you will have dialogue options that would contradict your personality. If, in this example, you playing as a *Soft* character choose rude options, more akin to a *Haphazard* character, your character's personality value may become *Haphazard*! This will be communicated likely by the previously mentioned one-sided [self-dialogue](#self-dialogue):  

> Self-dialogue: *"Hmm... I've been feeling more Haphazard lately..."*  

Of course, the biggest effect this would have on the game is changing how friendable and/or romanceable some NPCs are to you given your character's new personality value, as well as (potentially) changing what dialogue options are available to you.
