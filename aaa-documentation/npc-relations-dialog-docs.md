# NPC Relations and Dialogue Documentation

This document will cover specifically how NPC systems are coded.

## NPC Relationships  

The Character class posseses a dictionary in which an instance can keep track of other Character instances that it has met, knows, likes, hates, etc. This is laid out the same for both NPCs and the Player class, since both inherit from the parent Character class.  

`Character.contacts` is the name of this dictionary, and belonging to the dictionary are a total of ten keys which each represent a different kind relationship another character can have with each Character instance. For purposes of narrative differentiation (though each of these following two categories are also treated slightly differently in the code), these relationship keys can be thought of as either **"platonic"** or **"romantic"**. The platonic keys are `knows`, `friends`, `bestfriends`, `dislikes`, and `hates`. The romantic relationship keys are `into`, `romantic`, `serious`, `exromantic`, and `exserious`. Each of these keys possess lists. The Player's dictionary will likely begin empty, and populate as the Player interacts with NPCs. NPC's contacts dictionary will start pre-filled as part of their character writing. Other NPCs that they know, like, dislike, etc. will be written with the rest of their character. Each character in each list will be represented as a **two-length tuple**, with the first element being the reference to a Character and the second being the [friendship score](#quick-aside-friendship-score) the instance has with the Character in question.  

Note: moving forward in this section, the Character instance who possesses the dictionary will be referred to as **"Self"**, **"the instance"**, or **"the Self instance"**. The Character instance that is referenced in the Self instance's contacts dictionary will be referred to as **"the Character in question"** or just **"the Character"**.

### Quick Aside: Friendship Score

The **Friendship Score** or perhaps put more neutrally, **Relationship Score** is an integer value depicting exactly how close a Character is to the Self instance. As noted earlier, this value will accompany the Character reference in a tuple within the list value that's paired with one of the relationship keys in the `Character.contacts` dictionary.

```
contacts = {
    "knows": [
        (<Character>, friendship_score),
        (<Character>, friendship_score),
        (<Character>, friendship_score)
    ],
    ...
}
```
*Example of the layout of the `Character.contacts` dictionary*.

---

### Platonic Relationship Keys

### `knows`

The `knows` key will narratively represent Characters that Self has met, but not quite made friends with just yet.  

Characters are added to `knows` with a base Friendship score of 10. In general, the threshold for upgrading a friendship level is **25** and the threshold for downgrading a friendship level is, naturally, **0**.  

If the Friendship level is increased beyond 25, the Self instance's relationship with a Character will upgrade to `friends`.  
It is impossible for a Character to be forgotten in this NPC relationship system-- either a Character will have to be manually moved to a negative platonic relationship key like `dislikes` or `hates`, or they will always just remain as someone Self is, at second-worst, distantly familiar with.  

The implications of this include but are not limited to this universe's Goatye never being able to make the 2011 hit ["Somebody That I Used To Know"](https://youtu.be/8UVNT4wvIGY?si=fx3COLQifdlnBlac), as again, the way the code is set up makes it impossible to ever not know someone after meeting them.

### `friends`

`friends` will naturally contain Characters that Self has become close enough to call.... well, Friends!!!!  

Regardless of how many points over 25 the increase of Friendship that upgraded the relationship to `friends` was (say if the Friendship score was at 22 and an increase of 5 took place, leaving a remainder over 25 of 2), the Friendship score will be set to **10** upon upgrading the relationship to `friends` from `knows`. Like `knows`, the Friendship score upgrade threshold for the `friends` relationship key will be **25** and the downgrade threshold will be **0**.  

*Small note*: the Friendship score can be either 0 or 25 no matter what the relationship key is. It's only when an `update_relationship()` call *(see the [`update_relationship()`](#characterupdate_relationship) Character class method)* is made with a Friendship score argument that would put the current score at either less than 0 or greater than 25 that an upgrade or downgrade of relationship status takes place.

Also note that `friends` is the first relationship key in a standard progression that has a natural downgrade possibility. While it is possible for any of these relationship keys, including `knows`, to be downgraded to `dislikes` or `hates`, those are technically special cases and will be covered shortly (see [`dislikes` & `hates`](#dislikes--hates)). If the Friendship score while Self is `friends` with a Character instance is made to go below 0, the two Characters will disconnect; the Character again becoming someone the Self instance only `knows`.  

An final note is that unlike being set to a default value of 10 when upgrading the relationship, DOWNGRADING from `friends` back to `knows` will see the Friendship score set to a measly 5. This is a common trope when downgrading relationship keys.

### `bestfriends`

If a Character who's `friends` with the Self instance becomes close enough that the Friendship score is made to go above 25, their relationship will once again upgrade to become `bestfriends`.  

Like `friends`, upon upgrading, the Friendship score will be set to a default value of **10**, and if the score is made to fall below 0, a relationship downgrade will take place. This downgrade from `bestfriends` back to `friends` will also see the Friendship score become **5** instead of 10 as it did when upgrading This is more consequential than the downgrade from `friends` to `knows` putting the score closer to 0 by normal, since losing all Friendship score as `knows` doesn't inherently downgrade the relationship. This is to more closely simulate a volatile friendship, as damaging a relationship as `bestfriends` won't immediately break the frienship *necessarily*, but it will put the relationship on thin ice, as it's by default closer than usual to losing the whole friendship.

### `dislikes` & `hates`

The negative platonic relationship keys are `dislikes` and `hates`. Both of these are not automatically downgraded to (with [one exception](#one-exception)), and need to be explicitly called to downgrade to using `update_relationship()` (see [explicit relationship traversal](#explicit-relationship-traversal)). That said, they ARE automatically upgraded out of, given the Friendship score increases enough to escape them.  

When downgraded to either `dislikes` or `hates`, the Friendship score is set to a predictable **5**. Also predictably, both relationship keys can be dug out of if the Friendship score is made to go above 25. This is, of course, a taller than usual order; in both cases, a Friendship increase of 20 is needed (since the score is set to 5 when a downgrade to either key happens), and an instance will be disinclined to engage in positive interactions with a Character they dislike or hate. Good luck!

#### One Exception

While it is true that `dislikes` cannot be automatically downgraded to, `hates` actually can be earned by having the Friendship score fall below 0 while Self `dislikes` a character.

---

### Romantic Relationship Keys

### `into`, `romantic` & `serious`

Narratively, `into` represents an instance being romantically interested in another Character, i.e. a crush, `romantic` represents an instance being in a romantically involved with another Character (or Characters!), and `serious` represents an instance being seriously involved with another Character romantically, such as being married or otherwise very steady.

Like `dislikes` and `hates`, all three of these romantic relationship keys are not achievable automatically-- they must be explicitly upgraded to. Again, see [explicit relationship traversal](#explicit-relationship-traversal).  

Unlike `dislikes` and `hates`, `into`, `romantic` and `serious` will not automatically downgrade to a lower key. Having the Friendship score with a Character an instance (the Player instance in particular) is `into`, `romantic` with, or `serious`ly romantic with fall below zero may open up the opportunity for perhaps an "I don't think this is working" cutscene, but won't automatically downgrade the relationship key.  

They ARE explicitly downgradable, of course. As the case with any relationship key, the romantic keys are downgradable to `dislikes` and `hates`, but also, a special third case exists for a clean breakup: as seen in [explicit relationship traversal](#explicit-relationship-traversal), an explicit downgrade to `bestfriends` is implimented. In the case of downgrading from a `romantic` or `serious` relationship, the Character instance the downgrade took place in reference to is added to the `exromantic` or `exserious` keys respectively. See below for details.

### `exromantic` & `exserious`

`exromantic` and `exserious` are special keys in that they will not contain a list of `(<Character>, friendship_score)` tuples, but rather simply a list of `<Character>` object references. They are also special in that the Character class methods that search through the `contacts` dictionary (like `audit_contact()` and `update_relationship()`) will not search these keys for Characters and thus not be able to return Characters that exist within these keys.  

Effectively, this puts the values in the `exromantic` and `exserious` keys in almost a separate environment- while a Character can only be in one place within the romantic and platonic keys (when an traversal takes place, the `(<Character> , friendship_score)` tuple is removed and placed in the list belonging to the relationship key that the traversal necessitates), once a Character reference is placed into either `exromantic` or `exserious`, it stays there basically forever.

---

### NPC Relationship-Related Class Methods

#### `Character.audit_contact()`

This Character.method takes in a Character to check the relationship to Self it has, and returns a tuple containing the relationship key that Character is found in within the Self instance's `contacts` dictionary, followed by the Friendship score for that relationship.

##### Parameters



#### `Character.update_relationship()`

This Character.method updates the relationship to another Character that the instance calling it has, using a

##### Parameters



##### Automatic Relationship Traversal



##### Explicit Relationship Traversal

