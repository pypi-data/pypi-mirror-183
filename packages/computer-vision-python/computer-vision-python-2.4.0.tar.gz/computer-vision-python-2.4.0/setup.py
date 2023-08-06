from distutils.core import setup
setup(
  name = 'computer-vision-python',         # How you named your package folder (MyLib)
  packages = ['computer_vision_python'],   # Chose the same as "name"
  version = '2.4.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'IT IS A VERY GOOD LIBRARY FOR COMPUTER VISION AND WHEN YOURE ARE MAKING THE PROJECT TRING',   # Give a short description about your library
  author = 'OM NIRMALKAR',                   # Type in your name
  author_email = 'info.craftfox@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Tring10/COMPUTERVISION/blob/main/mycv.zip',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Tring10/COMPUTERVISION/blob/main/mycv.zip',    # I explain this later on
  keywords = ['cv2', 'cv', 'tring','computer vision'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'opencv-python',
          'pyserial',
          'mediapipe',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)