# NERO - Fishing Anywere like a ninja!

<p align="center"> 
    <img src="/images/main.png">
</p>

Nero is an short but powerfull server to generate fake pages for phishing, doesn't come with pre-made webpages, Nero can retreive recursively and generate the SAME page and parse it quickly! Also, supports tunneling with Serveo, Ngrok and Tinyurl.

# Tutorial

It's super easy to configure! You just need to do the following:
<strong>set ip {your ip}</strong>
<strong>set port {your port}</strong> // default is 80, you can skip it if you want
<strong>set url {target url}</strong> 

You should have Ngrok instaled in your machine to sucefully get an 100% working URL. If not, will raise an error when you open the link generated.

# About bugs while grabbing passwords

Some domains may block the request because the Same Origin Policy is turned on. So, to bypass it, you need to set alternative urls for the current domain.
Examples:

https://somedomain.com/ 

to others alternatives: 

https://somedomain.com/login
https://web.somedomain.com/
...

## Advice

Usage of NERO for attacking targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program. Only use for educational purposes.

## LICENSE

NERO was made under GNU license. See license file for more.

## Insues

If you found an insue, please let me know!
