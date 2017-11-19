# JumpCloud_Exercises

Write 1 script that will enable/disable the “Guest” account on Windows: Enable_Disable_User.py
  - This script first checks if a "Guest" account exists on a Windows machine. If it does, it proceeds to check if the user has admin right. Once all conditions are met, the user has a choice of enabling or disabling the "Guest" acocunt.


Write 1 script that will enable the firewall (you choose which firewall) on a Linux system and allow incoming https/443 connections only: Enable_443_Only.py
  - This script checks if the user is running as root (i.e: sudo python Enable_443_Only.py). Then it proceeds to drop all INPUT, OUTPUT, FORWARD connections in order to just allow incomming https/443 connections only (as stated in the prompt).

      
