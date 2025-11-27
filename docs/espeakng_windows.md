espeak-ng Windows installation and usage guide
=====

To download the source code (or the codebase) of espeak-ng, do the following steps:

1. Go to https://github.com/espeak-ng/espeak-ng

![](https://pad.hhu.de/uploads/d850e87e-36f7-42b0-b620-6e0fb179913c.png)

2. Click on Code (in green)

![](https://pad.hhu.de/uploads/7650a86d-faab-4e6b-a794-1a111edbe721.png)

3. Click on Download ZIP

![](https://pad.hhu.de/uploads/1410b3b6-ec1d-41d4-a781-369aa47ecf2d.png)

4. Save the folder as espeak-ng.zip and click on save

![](https://pad.hhu.de/uploads/4ea4dc65-3368-4d78-b56a-737acafab2f3.png)

5. Extract the folder from the zip file and make sure that the name of the folder is `espeak-ng` and click on `Extract`

![](https://pad.hhu.de/uploads/25756890-4916-471a-8523-6c3774ebd807.png)

6. You should then be able to see the espeak-ng folder and espeak-ng-master folder inside it. Rename this folder as `espeak-ng` too 

![](https://pad.hhu.de/uploads/1c24165b-04cd-4068-897f-615bfb8b01cf.png)

7. At the end, you should be able to see espeak-ng folder inside espeak-ng folder:

![](https://pad.hhu.de/uploads/129a7eb4-c652-4157-9389-5040750c4c16.png)


Great, now you have the source code (or the codebase)!


----------------


Installing espeak-ng
-------------------

1. Go to https://github.com/espeak-ng/espeak-ng . Locate `Releases` on the right side as shown in the screenshot and click on the number. Note that the release number might vary, but please click on it irrespectively

![](https://pad.hhu.de/uploads/d45dba5e-4042-4320-8726-d69c4032767e.png)

2. Once you click on the number, scroll down to the bottom of the page and locate the file `espeak-ng.msi` and click on it

![](https://pad.hhu.de/uploads/02bcc3b2-14d8-4c93-8453-7416194c05f0.png)

3. Download the above file into your Downloads folder

![](https://pad.hhu.de/uploads/e9e82327-8296-48e8-ae53-0f1d5b9ff426.png)

4. Double click on the `espeak-ng.msi` file

![](https://pad.hhu.de/uploads/ffeea2b7-ca92-4c61-acda-f01361501cae.png)

NOTE: If you get a message saying that whether you trust the unknown publisher, please go ahead and click on `Run anyway`  

5. Accept the license

![](https://pad.hhu.de/uploads/3afb72d8-f011-4ebd-9e9b-5ba81781dfb2.png)

6. Press `Next`

![](https://pad.hhu.de/uploads/7744bd72-15fa-4257-bdfe-42b3a4b826c8.png)

7. Press `Install`

![](https://pad.hhu.de/uploads/134dc1da-9592-4e26-b2cd-d0a474da60a0.png)


---------------

Adding a new language (Part 1)
---------------------

1. Locate OS(C:)

![](https://pad.hhu.de/uploads/fedb2e4f-de86-4937-acd7-5c727652aed8.png)

2. Click on Program Files 

![](https://pad.hhu.de/uploads/905d5102-2050-47ce-9077-aad61e3c4086.png)

3. Locate eSpeak NG

![](https://pad.hhu.de/uploads/8a921b00-dce8-490b-b6fd-b533ef7ca08c.png)

4. Right click and go to `Properties` 

![](https://pad.hhu.de/uploads/2a1cf2b8-49ee-4521-ab2b-9a9075008af7.png)

5. Click on `Security`

![](https://pad.hhu.de/uploads/1f092c4d-0b31-4139-8514-bd8687d8c81c.png)

6. Click on `Edit`

![](https://pad.hhu.de/uploads/98f8ec48-e733-48b7-8ed7-20bb430da1cd.png)

7. Locate Benutzer and click below `Allow` and then click on `Apply` followed by `OK`

![](https://pad.hhu.de/uploads/4bf4b315-1eb8-4ecd-9ae4-0fc51f39e11a.jpg)

8. Go inside eSpeak NG folder and you should be able to see these files and folders:

![](https://pad.hhu.de/uploads/720b0d8b-92ef-4fbe-aa43-2dbde5596951.png)

9. Now again go to Downloads and locate espeak-ng and double click. You should find another espeak-ng folder, if so, double click and you should be able to find these files and folders:

![](https://pad.hhu.de/uploads/eeddbd6d-8953-444b-8c18-8146da2f21b8.png)

-----------

Installing sublime text editor
---------------------------

If you do not have sublime text editor installed, please follow the steps below, otherwise, continue to the next section.

1. Go to https://www.sublimetext.com/ and click on Download for Windows

![](https://pad.hhu.de/uploads/75b95955-08f1-4278-b3f2-cc88a96e9972.png)

2. Download 

![](https://pad.hhu.de/uploads/6f7917f3-09e4-487f-b4a9-09e6d8874b0c.png)

3. Click Next until it is installed

![](https://pad.hhu.de/uploads/845584bb-a919-47ef-8405-4aeea56812e6.png)


Adding a new language (Part 2)
------------------------

1. Open sublime text editor

![](https://pad.hhu.de/uploads/e0f25026-6f3b-4735-9082-5553b0a5ebd5.png)

2. Open the eSpeak-ng folder in your Downloads folder

![](https://pad.hhu.de/uploads/67d59bb0-8f4c-43a2-9a54-a5a1e7fc943d.png)

3. Go to sublime text editor. Click on `espeak-ng-data` on the left hand side and click on `lang` followed by `art`

![](https://pad.hhu.de/uploads/2ddbdc4c-ecdc-4abd-b34e-869363e0d576.png)

4. Click on `File` and `New file` and copy the contents by replacing the name of the language (in my case `toy`) to yours. 

![](https://pad.hhu.de/uploads/818a41fc-d326-4c3a-bc28-fd822015c0a6.png)

5. Click on `File` and `Save as`

![](https://pad.hhu.de/uploads/38fb3afd-b0d7-4fc0-8bd0-778b49f62fc5.png)

6. Make sure that you are saving as the name of your language and check the folder - the file should exactly be in the art folder as shown below

![](https://pad.hhu.de/uploads/f15a212c-fea9-4be0-a5a1-78492b962cfd.png)

7. Find the `phsource` folder on the left and side and click on the folder

![](https://pad.hhu.de/uploads/5bdb31fe-6071-4086-89e4-dedf06a2cbfc.png)

8. Add a new file under `phsource` folder

![](https://pad.hhu.de/uploads/ae692b58-e298-4f86-bf3a-bc2cdd7866ed.png)

9. Save as `ph_toy` inside the `phsource` folder

![](https://pad.hhu.de/uploads/768497fd-e66e-4d12-8858-8b427bcdc84a.png)

![](https://pad.hhu.de/uploads/dd0c0c38-52eb-4ce6-a0e1-913011a0fbbb.png)

10. Locate `phonemes` file on the left side and click on it. Add the below lines in line 1668 by replacing `toy` with your language name

![](https://pad.hhu.de/uploads/4c3ce7ce-5d45-4654-b49a-0d83a08f0fed.png)


11. Next, locate `dictsource` on the left side

![](https://pad.hhu.de/uploads/c09bd353-516a-4a1f-80d8-799b64fb13b6.png)

12. Create a new file as `toy_dict` (replace `toy` with your language name) and add a few entries

![](https://pad.hhu.de/uploads/22679fb7-dbf6-47a5-9065-ea1b85763702.png)

13. Add a few lexicons in a new file and save as `toy_list`

![](https://pad.hhu.de/uploads/ad144b23-b2cf-4990-bfc2-67107ddea9b1.png)

14. Save this file under `dictsource`

![](https://pad.hhu.de/uploads/c080d67d-2d10-4b9c-b446-02cb6240e747.png)

![](https://pad.hhu.de/uploads/e730c649-6d61-46d0-b082-d86069beaa0a.png)


15. Similarly, add a few rules by creating a new file

![](https://pad.hhu.de/uploads/8d8131cd-86d6-451f-accc-c718acb99895.png)

16. Save as `toy_rules` under `dictsource` folder

![](https://pad.hhu.de/uploads/b53c95ec-4aa7-485b-83c6-6381540e7d5c.png)

17. Locate `Makefile.am` on the left side and click on it

![](https://pad.hhu.de/uploads/57a027df-bbf1-44cc-a24f-802c0d1b030a.png)

18. Scroll down to line 446 and add the line (replace `toy` with your language name)

![](https://pad.hhu.de/uploads/741b054e-a5d7-4dcf-8ad6-723ef7ce98c9.png)

19. Scroll down to line 585 and add these line (replace `toy` with your language name)

![](https://pad.hhu.de/uploads/7aafff20-dde8-4d7d-bfe8-e427d5a2b078.png)


-------------------

Adding a new language (Part 3)
----------------------------

1. Copy the `dictsource` and `phsource` folders using Ctrl+c or Strng+c

![](https://pad.hhu.de/uploads/c1c45637-e5fb-4c74-9d85-19ccdf07813d.png)

2. Locate OS (C:) on the left side and click on it


![](https://pad.hhu.de/uploads/6a75fc83-6853-4b63-97f3-92c3c08dd2d4.png)

3. Click on `Program Files`

![](https://pad.hhu.de/uploads/aaff6bdd-066d-4c2c-b1de-8e7d1ee43b51.png)

4. Click on `eSpeak NG` folder

![](https://pad.hhu.de/uploads/a4cd332c-a815-4579-8665-b1c66fcbdc8e.png)

5. Paste the folders in this folder


![](https://pad.hhu.de/uploads/64c0d52e-5b3e-4ce7-a6aa-314c9295ba0d.png)

6. Now copy the language file similar to how you copied the folders. Go to Downloads > espeak-ng folder > espeak-ng folder and locate espeak-ng-data folder

![](https://pad.hhu.de/uploads/be71befc-aed0-4846-8098-bb6364e1648d.png)

7. Click on `lang` folder

![](https://pad.hhu.de/uploads/3c87b6af-76f2-4767-b7f5-49ca6345647e.png)

8. Click on `art` folder

![](https://pad.hhu.de/uploads/80195e98-f3bf-4229-b80f-01fcb8a4a02b.png)

9. Copy the `toy` file

![](https://pad.hhu.de/uploads/8d16dc13-85b2-4cb5-8e4a-d0b1b3feac8f.png)


10. Now go to `eSpeak NG` folder following: step 2,3 and 4

11. Locate `espeak-ng-data` and click on it

![](https://pad.hhu.de/uploads/e670a848-5bc6-4e4b-866a-48b30719d969.png)

12. Click on `lang` folder

![](https://pad.hhu.de/uploads/4513b658-06b2-4b55-8546-5b4923ea7e50.png)

13. Click on `art` folder

![](https://pad.hhu.de/uploads/f1de2d0b-9342-4afc-9b1e-db8b004b7d67.png)

14. Paste the `toy` file here (in your case, it should be your language name)

![](https://pad.hhu.de/uploads/07640db9-7695-4e54-9089-7ecc9a0cf384.png)


Compile using command prompt
-------------------

1. Open command prompt inside OS (C:) > Program Files > eSpeak NG

![](https://pad.hhu.de/uploads/6469ee77-3428-4495-8ffd-c3a5a7c7811f.png)

![](https://pad.hhu.de/uploads/a52861f0-a53a-42f0-baf1-fdeae6e7c58b.png)

2. Type this command to go inside the `phsource` folder and hit Enter

![](https://pad.hhu.de/uploads/3a0674c8-366a-4cc9-a425-ada05ef2eaf2.png)


3. Compile phonemes using this command and hit Enter

![](https://pad.hhu.de/uploads/ebb23941-6788-40ca-a7df-b981711de9fc.png)

![](https://pad.hhu.de/uploads/9d485e79-9fc8-4342-89b3-cc515545cdc8.png)

NOTE: you should see `0 errors` . If not, you have most likely skipped one of the steps from above. Please re-check. 

4. Let us compile the dictionary using the commands:

![](https://pad.hhu.de/uploads/20c6b656-8dc8-4cff-8d9a-191ab1cb9312.png)

hit Enter

![](https://pad.hhu.de/uploads/0bc60f47-c617-4517-a89c-a8a900d5af84.png)

Replace `toy` with the name of your language and hit Enter

NOTE: If you get any error message, you have most likely skipped one of the steps from above. Please re-check.

5. You can now start using your language

![](https://pad.hhu.de/uploads/9746ec37-47a2-47ad-9355-73c21b45e691.png)






