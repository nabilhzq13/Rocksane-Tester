# Hold photos

One real photo per hold type, shown in the Hold type picker, the technique examples and the Learn guide. All come from Wikimedia Commons under licences that allow use in the app, including the paid edition, with credit. Each was cropped to a square and resized to 480 px (WebP). The cropped versions are shared under the same licence as the original. The app lists these credits in the Learn tab (from `HOLD_PHOTO` in `src/holds.js`).

| Type | Original | Author | Licence | Changes |
|---|---|---|---|---|
| Jug | [Indoor Climbing Holds 2.jpg](https://commons.wikimedia.org/wiki/File:Indoor_Climbing_Holds_2.jpg) | uncarved block | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/) | cropped |
| Crimp | [Leistenklettern.jpg](https://commons.wikimedia.org/wiki/File:Leistenklettern.jpg) | Anna reg | [CC BY-SA 3.0 AT](https://creativecommons.org/licenses/by-sa/3.0/at/deed.en) | cropped |
| Sloper | [Thomasp auflegegriff.jpg](https://commons.wikimedia.org/wiki/File:Thomasp_auflegegriff.jpg) | Thomas Pinz (ThomasP) | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) | cropped |
| Pinch | [Thomasp zangengriff.jpg](https://commons.wikimedia.org/wiki/File:Thomasp_zangengriff.jpg) | Thomas Pinz (ThomasP) | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) | cropped |
| Pocket | [Mono hold.jpeg](https://commons.wikimedia.org/wiki/File:Mono_hold.jpeg) | Jarekt Tuszyński | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | cropped |
| Sidepull | [The Buttermilk Boulders - 15290712346.jpg](https://commons.wikimedia.org/wiki/File:The_Buttermilk_Boulders_-_15290712346.jpg) | MarkDoliner | [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/) | cropped |
| Gaston | [Baboon's Athlete Bella Jariel on Karajo V11(8a).jpg](https://commons.wikimedia.org/wiki/File:Baboon%27s_Athlete_Bella_Jariel_on_Karajo_V11(8a).jpg) | Adanxmorales | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | cropped, shirt logo blurred |
| Undercling | [Thomasp untergriff.jpg](https://commons.wikimedia.org/wiki/File:Thomasp_untergriff.jpg) | Thomas Pinz (ThomasP) | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) | cropped |
| Volume | [ClimbingHolds 20211103 145113.jpg](https://commons.wikimedia.org/wiki/File:ClimbingHolds_20211103_145113.jpg) | Ka23 13 | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | cropped |

To replace a photo: put a square 480 px WebP at `web/holds/<type>.webp`, update its entry in `HOLD_PHOTO` (`src/holds.js`) and this table, then run `python build.py`.
