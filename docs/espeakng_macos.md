espeak-ng macOS guide
===================

Installation
------------

1. Open terminal using spolight (command+spacebar) and search terminal

![](https://pad.hhu.de/uploads/42ab780e-00f7-4fe8-a282-35cc33111004.png)

2. Terminal should look like this

![](https://pad.hhu.de/uploads/199d9f2b-2b0e-4072-99f0-e781f2bea360.png)


3. Copy the entire link and paste it inside the terminal

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

![](https://pad.hhu.de/uploads/4d1d73e9-91d4-4e9d-abf7-b28495efa61d.png)

and hit Enter

4. Hit Enter once you see this

![](https://pad.hhu.de/uploads/6b3d62d9-10f4-4d28-954e-546c42df6926.png)

5. Progress looks like this... and this will take a few minutes to install

![](https://pad.hhu.de/uploads/c74b885b-557d-43c5-913a-a7171b293992.png)

6. Install espeak-ng using the command:

![](https://pad.hhu.de/uploads/078807d1-b153-476b-8188-d27ac158403e.png)

and hit Enter

7. Test if espeak-ng is working (make sure that your sound is turned on) using

![](https://pad.hhu.de/uploads/013c38d9-aacb-4809-b66f-acaa03f72d58.png)

you should hear "hello world"

-------

Download source code (or codebase)
=============

1. Go to https://github.com/espeak-ng/espeak-ng and click on code

![](https://pad.hhu.de/uploads/8a99b07e-1f70-41b9-965f-14ba49ef4287.png)

2. Click on Download ZIP and save as espeak-ng

![](https://pad.hhu.de/uploads/32eacf0b-4491-449a-b5da-4168dee8d160.png)

3. Extract the folder and rename the folder to espeak-ng. The contents inside this folder must look this

![](https://pad.hhu.de/uploads/6c68d2f2-8834-4c37-9759-eecf1144e87e.png)

---------------

Installing and using sublime text editor
=================

1. Go to https://www.sublimetext.com/ and click on Download for Mac

2. Save the file

![](https://pad.hhu.de/uploads/9d94a397-fc50-44f1-971e-19bdaae1d644.png)

3. Install by clicking on the downloaded file

4. Double clock on the sublime text icon and close this window that has text like "Stable Channel ..."

![](https://pad.hhu.de/uploads/9d4035c3-9e33-4a56-97f2-9150d90589f4.png)

5. Open the espeak-ng folder that is saved on the desktop by clicking on Open

![](https://pad.hhu.de/uploads/b78cb2a4-02ba-4379-b071-53915ecd199e.png)

6. Click on Macintosh HD

![](https://pad.hhu.de/uploads/d34f444e-7481-4465-add7-607851623f07.png)

7. Click on Desktop

![](https://pad.hhu.de/uploads/6b5c383f-7f9a-44fe-b6da-b24bb1a83e9b.png)

8. Click on espeak-ng folder and press open

![](https://pad.hhu.de/uploads/800a9d3c-4053-421b-b41f-44111e8cde9c.png)

9. Once you open, you must see a screen like this

![](https://pad.hhu.de/uploads/fe46d728-7093-4e03-8978-b632df2d7a40.png)



Adding a new language (Part 1)
============

1. Locate espeak-ng-data folder on the left side of the sublime text editor and click on it

![](https://pad.hhu.de/uploads/59a79672-eee9-4e36-89be-b0f90ac9c388.png)

2. Click on lang folder

![](https://pad.hhu.de/uploads/b1d5db0b-be0a-470d-9f6d-c54c1e543b50.png)

3. Click on art folder inside lang folder

![](https://pad.hhu.de/uploads/0ffa2f5c-e9bb-4100-8787-f4a153e13202.png)

4. Create a new file

![](https://pad.hhu.de/uploads/459773d1-805c-483e-a71e-e74783710684.png)

5. Define your language name

![](https://pad.hhu.de/uploads/8b7f2907-a7c5-4804-b6c7-b379e5f41866.png)

You need to replace toy with your language name

6. Click on File and go to Save as..

![](https://pad.hhu.de/uploads/7d14558f-c38a-4d15-b558-2679b0ca9f2f.png)

7. Save as the name of your language. In my case, it is toy. Make sure you are saving it inside the art folder

![](https://pad.hhu.de/uploads/f74b224f-1478-40f7-aafd-133a629db2d0.png)

![](https://pad.hhu.de/uploads/f505017f-b792-4b25-a318-d1322959efc5.png)

Adding Phonemes
-----------

1. Locate phsource folder on the left side of the sublime text editor and click on it

![](https://pad.hhu.de/uploads/12faf591-f1cf-4832-8166-96cf7414f12a.png)

2. Create a new file

![](https://pad.hhu.de/uploads/40959401-8b21-42d4-92bb-94562febfe2a.png)

3. Copy the content (phonemetable toy base1) to the file

![](https://pad.hhu.de/uploads/7f06d00d-ee65-402d-a605-c84ee6008685.png)

4. Save this as ph_toy (replace toy with your language name) inside phsource folder

![](https://pad.hhu.de/uploads/6cb5bc2f-73ba-4521-8fa1-2a094591e94f.png)

5. Locate the phonemes file

![](https://pad.hhu.de/uploads/a592887b-d3bd-4712-ac24-64f340b6f030.png)

6. Click on it and go to line 1670 and the below two lines

![](https://pad.hhu.de/uploads/331b2347-9573-4e3c-b6e2-1959af1efc6f.png)

------------

Adding lexicons and rules
-----------------------

1. Scroll up on the left side of sublime text editor and locate dictsource

![](https://pad.hhu.de/uploads/de14516f-10c9-4316-ab7f-427d05eb1dc3.png)

2. Create a new file

![](https://pad.hhu.de/uploads/bcba1b77-b9b7-4e3f-9846-4eab470f75a6.png)

3. Add a few entries, make sure you use a tab to seperate the word on the left and the right

![](https://pad.hhu.de/uploads/1aa2ede9-361f-49b5-bf4a-415103e3658b.png)


4. Save this file under dictsource as your language name followed by underscore and list. In my case it is toy_list

![](https://pad.hhu.de/uploads/21ecb7f7-8be0-4919-8373-7bc46df274c7.png)

5. Create a new file

![](https://pad.hhu.de/uploads/4ed6b116-e61f-43c4-8fe6-3a95e56a5c4d.png)

6. Write a few rules

![](https://pad.hhu.de/uploads/915ae3b4-6282-4208-a3da-5563126f9c29.png)


7. Save this file under dictsource as your language name followed by underscore and rules. In my case it is toy_rules

![](https://pad.hhu.de/uploads/0421a253-cd04-443f-86ec-1b227e80de47.png)

------------

Copying these files to where espeak-ng is installed
-------------

1. Copy this text and paste in your spotlight and double click on espeak-ng-data

/opt/homebrew/Cellar/espeak-ng/1.52.0/share/espeak-ng-data

![](https://pad.hhu.de/uploads/8d6eccb8-258a-4812-b9d4-142ee9585683.png)

2. When you open this, you should see these files in the above folder

![](https://pad.hhu.de/uploads/59fcb299-8e87-435e-a5e9-1448db3de79c.png)

3. Locate lang folder and locate the art folder inside it 

3. Now open the codebase that we changed that is in your desktop


4. Locate the espeak-ng-data folder and click on it

![](https://pad.hhu.de/uploads/e4e63a5a-3298-4ac4-be55-e098ff88fcc4.png)

5. Click on lang folder

![](https://pad.hhu.de/uploads/d4398742-dcf7-4995-935c-41026fb69b64.png)

6. Click on art folder and locate your language file. In my case it is toy and copy this file

![](https://pad.hhu.de/uploads/12c0186d-655a-420d-bd27-353a25bb6675.png)


7. Paste this file in the lang folder in the folder that you opened in Step 3

![](https://pad.hhu.de/uploads/9a5046be-fac1-4342-bd27-5b992127ded4.png)


8. Similarly copy the folders phsource and dictsource

![](https://pad.hhu.de/uploads/0c6142c5-6518-4c5a-8a9e-c9f83180f20e.png)

9. Now come back to the other window and go back to the espeak-ng-data by clicking back twice from the window that you opened in Step 7, so you should be able to see files like these

![](https://pad.hhu.de/uploads/d245b791-66c6-439d-9370-5e937c6f43b7.png)


10. Paste the two folders here

![](https://pad.hhu.de/uploads/8ce35da3-1d94-4f6b-8964-c38f1b34d9cf.png)

---------------------

Compiling the new language
----------------------

1. Open terminal and type 

cd /opt/homebrew/Cellar/espeak-ng/1.52.0/share/espeak-ng-data

![](https://pad.hhu.de/uploads/687e184a-a598-4b0c-89cc-2938fabc8ac2.png)

and hit enter

2. type:

mv phsource ../

![](https://pad.hhu.de/uploads/e7cbf057-2c1f-482b-80fc-f234b75393cc.png)

and hit enter

3. type:

espeak-ng --compile-phonemes

and hit enter

![](https://pad.hhu.de/uploads/9e15df52-1c7e-4f50-86db-0bacbf8af723.png)

You should get 0 errors. If not, repeat the above steps.

4. Next, let us compile the dictionary and the rules. type:

cd dictsource/

![](https://pad.hhu.de/uploads/d4a1eab9-3ae6-4d1b-b057-e7e6c3d34b24.png)

and hit enter

5. type:

espeak-ng --compile=toy

![](https://pad.hhu.de/uploads/de4ae9e1-ef14-4449-bcef-417474e624d6.png)


6. Test if your language is working:

espeak-ng -v toy "bear"

![](https://pad.hhu.de/uploads/61701ca4-0176-498f-8a2f-f05f84da5807.png)

replace toy with your language name

-------------------


