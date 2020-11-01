# Gnewsapi
Gets the Headlines and source url of articles from gnews

Download the code on ur local pc and run the app.py with all the required modules installed

```  required modules:
     bs4
     flask
     requests
   ``` 
    
    
After sucessful run ,the app will be seen running on:
 
  ``` http://127.0.0.1:5000 ```   
   
   Now to acess the news type any of below keywords:
   
   ```
    india
    world
    technology
    science
    sports
    health
    entertainment
    bengaluru
    newdelhi
    mumbai
    patna
    hyderabad
    chennai
    
    http://127.0.0.1:5000/?q=india
    
   or give the topic link from gnews ex:
   https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen
   
   http://127.0.0.1:5000/?q=https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen
   
   ```
   
   sample responses:
   
   ```[
  {
    "head": "Bypolls Not About Power But Respect For Gwalior-Chambal: Jyotiraditya Scindia",
    "link": "https://news.google.com/articles/CAIiEA_rbftW8fAfg9ZFOyAM-rwqGQgEKhAIACoHCAowj8n_CjDIrfkCMPGi6AU?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "‘Don’t forget those who questioned existence of Ram,’ PM Modi in West Champaran",
    "link": "https://news.google.com/articles/CAIiENPpvYYFnRn2sk6KeTW5oUAqFggEKg4IACoGCAoww7k_MMevCDDpywE?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "TN extends lockdown till November 30: Activities allowed and restricted",
    "link": "https://news.google.com/articles/CAIiECI6JjQsQlVT7FKFlF3cX3MqGQgEKhAIACoHCAow7pf_CjDdlfgCMP2F6gU?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Trying to be ‘BJP lite’ will end up making Congress zero, says Shashi Tharoor",
    "link": "https://news.google.com/articles/CBMiamh0dHBzOi8vc2Nyb2xsLmluL2xhdGVzdC85NzczNzcvdHJ5aW5nLXRvLWJlLWJqcC1saXRlLXdpbGwtZW5kLXVwLW1ha2luZy1jb25ncmVzcy16ZXJvLXNheXMtc2hhc2hpLXRoYXJvb3LSAW5odHRwczovL2FtcC5zY3JvbGwuaW4vbGF0ZXN0Lzk3NzM3Ny90cnlpbmctdG8tYmUtYmpwLWxpdGUtd2lsbC1lbmQtdXAtbWFraW5nLWNvbmdyZXNzLXplcm8tc2F5cy1zaGFzaGktdGhhcm9vcg?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Complete shutdown in Valley against land laws",
    "link": "https://news.google.com/articles/CAIiEEGpaFpoldJxPVLwHMdaik0qGQgEKhAIACoHCAowyo-HCzD-tIUDMIbRlgY?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "NASA images show sudden rise in stubble burning cases in Punjab, Haryana",
    "link": "https://news.google.com/articles/CAIiEHSW1-_b3HxpzP6HAgdvprcqGQgEKhAIACoHCAowr6n9CjCr4PQCMN791QM?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "\"Vote For Hand Symbol\": Jyotiraditya Scindia's Faux Pas At Rally",
    "link": "https://news.google.com/articles/CAIiEHS9qA7J94ScNO0e7YupYE0qGQgEKhAIACoHCAowj8n_CjDIrfkCMJWZ2AY?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Gujjar body, Rajasthan cabinet sub-panel agree on 14 points, stir called off",
    "link": "https://news.google.com/articles/CAIiEOIcnFOdl0ZvrvDxIJb2UG0qFggEKg4IACoGCAoww7k_MMevCDDpywE?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Sedition case filed against Jharkhand BJP chief for trying to ‘destabilise’ state govt",
    "link": "https://news.google.com/articles/CAIiEH4fGs5gl2rzei0f9aMIhdUqFwgEKg4IACoGCAoww7k_MMevCDC7rdgG?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Amid outrage over Ballabhgarh incident, Anil Vij says Haryana mulling law against ‘love jihad’",
    "link": "https://news.google.com/articles/CAIiEDYEjaaanmztqwTdhUDpAToqGAgEKg8IACoHCAow3rvTBDD89X4w8ZXmBQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Captured in Wayanad, tigress escapes from cage in Kerala’s Neyyar Safari Park",
    "link": "https://news.google.com/articles/CAIiEBU57yruPygja6UsdhT6IM4qFggEKg4IACoGCAoww7k_MMevCDDpywE?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Not involved in Pulwama attack, says Pakistan",
    "link": "https://news.google.com/articles/CAIiEIdvS4ELGaTBumqWQ91ACDUqGQgEKhAIACoHCAowyo-HCzD-tIUDMLfhlgY?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Mumbai local train update: Railways to run 2020 suburban services from today. Check route, other details",
    "link": "https://news.google.com/articles/CAIiEOfbWOFUHJyZKRGugA0GBF8qFwgEKg4IACoGCAowxLQ_MNevCDCyrdsG?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "India Sees 1-Day Surge Of 46963 Covid Cases, Over 81 lakh Total Cases",
    "link": "https://news.google.com/articles/CAIiEJQxWYywORYMujToKm_LvAoqGQgEKhAIACoHCAowj8n_CjDIrfkCMJWZ2AY?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "As Bihar moves into phase-2, Tejashwi puts up tough fight",
    "link": "https://news.google.com/articles/CAIiEJDm0mkx_IlTWs-uOYBn1h4qGQgEKhAIACoHCAowzrL9CjDC7vQCMK2y1gU?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "10 cities with least air pollution in India",
    "link": "https://news.google.com/articles/CAIiECkW8ctQ9UCw50agYyZVtt0qGQgEKhAIACoHCAowr6n9CjCr4PQCMN791QM?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Hizbul Muhajideen chief commander Saifullah killed in encounter in Kashmir’s Rangreth; police laud ‘huge...",
    "link": "https://news.google.com/articles/CAIiEOKz039L3wOE5mGIZroPTAMqFggEKg4IACoGCAoww7k_MMevCDDpywE?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Lockdown Extension in India: Odisha extends lockdown in containment zones till November 31",
    "link": "https://news.google.com/articles/CAIiECagUSYr6Xow2GEIP0hrjCQqGQgEKhAIACoHCAow55veCjDzvdUBMIPh5gU?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "SpiceJet gets 3000 bookings after PM Modi launches seaplane service in Gujarat - Details here",
    "link": "https://news.google.com/articles/CAIiEIzTuzABB9DZsb7pjHCKo_gqGQgEKhAIACoHCAowib-NCzDawJ8DMLXSpwY?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Modi in Gujarat: Is BJP Worried About Cong’s Revival in Bypolls?",
    "link": "https://news.google.com/articles/CAIiECkLiMN7gzXnCWvm61kBJmMqGQgEKhAIACoHCAowwqP5CjDypeECMI6VwgU?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Photos: Delhi markets full of shoppers despite rise in Covid-19 cases",
    "link": "https://news.google.com/articles/CBMilwFodHRwczovL3d3dy5oaW5kdXN0YW50aW1lcy5jb20vcGhvdG9zL2RlbGhpLW5ld3MvcGhvdG9zLWRlbGhpLW1hcmtldHMtZnVsbC1vZi1zaG9wcGVycy1kZXNwaXRlLXJpc2UtaW4tY292aWQtMTktY2FzZXMvcGhvdG8tbGY3Z2J0VEJCYXU5RUFITGhFRWdESi5odG1s0gGbAWh0dHBzOi8vbS5oaW5kdXN0YW50aW1lcy5jb20vcGhvdG9zL2RlbGhpLW5ld3MvcGhvdG9zLWRlbGhpLW1hcmtldHMtZnVsbC1vZi1zaG9wcGVycy1kZXNwaXRlLXJpc2UtaW4tY292aWQtMTktY2FzZXMvcGhvdG8tbGY3Z2J0VEJCYXU5RUFITGhFRWdESl9waG90by5odG1s?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Jagan Reddy’s SOS to PM Modi after finance ministry throws a spanner in Polavaram project",
    "link": "https://news.google.com/articles/CAIiEMxVRc4GH6c-s8m3F7vYHX8qFggEKg4IACoGCAoww7k_MMevCDDpywE?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "GST collections cross ₹ 1 lakh crore in Oct for first time in 8 months",
    "link": "https://news.google.com/articles/CBMiggFodHRwczovL3d3dy50aGVoaW5kdS5jb20vYnVzaW5lc3MvRWNvbm9teS9nc3QtY29sbGVjdGlvbnMtY3Jvc3MtMS1sYWtoLWNyb3JlLWluLW9jdC1mb3ItZmlyc3QtdGltZS1pbi04LW1vbnRocy9hcnRpY2xlMzI5OTU4NzcuZWNl0gGHAWh0dHBzOi8vd3d3LnRoZWhpbmR1LmNvbS9idXNpbmVzcy9FY29ub215L2dzdC1jb2xsZWN0aW9ucy1jcm9zcy0xLWxha2gtY3JvcmUtaW4tb2N0LWZvci1maXJzdC10aW1lLWluLTgtbW9udGhzL2FydGljbGUzMjk5NTg3Ny5lY2UvYW1wLw?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "High-voltage electioneering for Dubbak bypolls ends today",
    "link": "https://news.google.com/articles/CBMibWh0dHBzOi8vd3d3LmRlY2NhbmNocm9uaWNsZS5jb20vbmF0aW9uL3BvbGl0aWNzLzAxMTEyMC9oaWdoLXZvbHRhZ2UtZWxlY3Rpb25lZXJpbmctZm9yLWR1YmJhay1lbmRzLXRvZGF5Lmh0bWzSAXFodHRwczovL3d3dy5kZWNjYW5jaHJvbmljbGUuY29tL2FtcC9uYXRpb24vcG9saXRpY3MvMDExMTIwL2hpZ2gtdm9sdGFnZS1lbGVjdGlvbmVlcmluZy1mb3ItZHViYmFrLWVuZHMtdG9kYXkuaHRtbA?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Ties with China under Severe Stress, Bid to Change Status Quo of LAC 'Unacceptable': EAM Jaishankar",
    "link": "https://news.google.com/articles/CAIiENGRSLI0eN-pReGrPCEumxsqGQgEKhAIACoHCAow5qqNCzD4q58DMPbXpwY?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "A Secularist, Sardar Patel Had United India In Spite of Travancore's 'Hindu God' Excuse",
    "link": "https://news.google.com/articles/CAIiEEi5JZiAyumBx4ANJxRFfKAqMwgEKioIACIQukpDkFnrHbDQGyBDxSojnyoUCAoiELpKQ5BZ6x2w0BsgQ8UqI58w37jrBg?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "J&K administration annuls Roshni Act, to retrieve land within six months",
    "link": "https://news.google.com/articles/CAIiEGBX-ZK6_qCJw09MQtzG-kQqGQgEKhAIACoHCAowr6n9CjCr4PQCMN791QM?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Covid-19 vaccine predictions of pharma companies that didn’t come true",
    "link": "https://news.google.com/articles/CAIiEBbZow-RSEoYiyUcD-bPK54qFggEKg4IACoGCAoww7k_MMevCDDl2wE?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Karnataka govt mulls Kannada test to shore up jobs for locals",
    "link": "https://news.google.com/articles/CAIiEDAVJ0v0YjAEK4Iibq8W8DQqGQgEKhAIACoHCAowzrL9CjDC7vQCMK2y1gU?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Will send Congress MLA Sherman Ali Ahmed to jail after polls for lungi comment: Himanta Biswa Sarma",
    "link": "https://news.google.com/articles/CAIiEPvfZZJIO-F2KLRhsUyJ7s8qGAgEKg8IACoHCAowop2lATDj4RowwtDJBQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Bengaluru drug case: Anoop Bineesh’s ‘benaamidar’, says ED",
    "link": "https://news.google.com/articles/CBMigAFodHRwczovL3d3dy5uZXdpbmRpYW5leHByZXNzLmNvbS9jaXRpZXMvYmVuZ2FsdXJ1LzIwMjAvb2N0LzMxL2JlbmdhbHVydS1kcnVnLWNhc2UtYW5vb3AtYmluZWVzaHMtYmVuYWFtaWRhci1zYXlzLWVkLTIyMTc0MzYuaHRtbNIBf2h0dHBzOi8vd3d3Lm5ld2luZGlhbmV4cHJlc3MuY29tL2NpdGllcy9iZW5nYWx1cnUvMjAyMC9vY3QvMzEvYmVuZ2FsdXJ1LWRydWctY2FzZS1hbm9vcC1iaW5lZXNocy1iZW5hYW1pZGFyLXNheXMtZWQtMjIxNzQzNi5hbXA?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Impossible to stop COVID spread through lockdown, treat mask as vaccine: Jain",
    "link": "https://news.google.com/articles/CAIiEDDcvnkvrHfWTrzkXW8WmgwqFwgEKg4IACoGCAowxLQ_MNevCDCyrdsG?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "[Watch] 4-year-old Mizoram girl sings AR Rahman's Vande Mataram, catches PM Modi's attention",
    "link": "https://news.google.com/articles/CAIiEEgGMCuKPkgaJw2H9P5OZwQqGQgEKhAIACoHCAowlbCPCzCrzaIDMLbgrgY?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Telangana braces up to face surge in Covid-19 cases",
    "link": "https://news.google.com/articles/CBMidGh0dHBzOi8vd3d3LmRlY2NhbmNocm9uaWNsZS5jb20vbmF0aW9uL2luLW90aGVyLW5ld3MvMDExMTIwL3RlbGFuZ2FuYS1icmFjZXMtdXAtdG8tZmFjZS1zdXJnZS1pbi1jb3ZpZC0xOS1jYXNlcy5odG1s0gF4aHR0cHM6Ly93d3cuZGVjY2FuY2hyb25pY2xlLmNvbS9hbXAvbmF0aW9uL2luLW90aGVyLW5ld3MvMDExMTIwL3RlbGFuZ2FuYS1icmFjZXMtdXAtdG8tZmFjZS1zdXJnZS1pbi1jb3ZpZC0xOS1jYXNlcy5odG1s?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "4th cutoff out, seats vacant even in popular DU colleges",
    "link": "https://news.google.com/articles/CBMif2h0dHBzOi8vdGltZXNvZmluZGlhLmluZGlhdGltZXMuY29tL2NpdHkvZGVsaGkvNHRoLWN1dG9mZi1vdXQtc2VhdHMtdmFjYW50LWV2ZW4taW4tcG9wdWxhci1kdS1jb2xsZWdlcy9hcnRpY2xlc2hvdy83ODk3NjEzNC5jbXPSAXpodHRwczovL20udGltZXNvZmluZGlhLmNvbS9jaXR5L2RlbGhpLzR0aC1jdXRvZmYtb3V0LXNlYXRzLXZhY2FudC1ldmVuLWluLXBvcHVsYXItZHUtY29sbGVnZXMvYW1wX2FydGljbGVzaG93Lzc4OTc2MTM0LmNtcw?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "17-yr-old girl in Vizag found dead with her throat slit amid wedding celebrations",
    "link": "https://news.google.com/articles/CAIiEEap-lmT_8KnWv7yumdoZPoqGQgEKhAIACoHCAow7pf_CjDdlfgCMNyH6gU?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Karnataka CM Yediyurappa promises cabinet berth for Munirathna on bye-poll victory",
    "link": "https://news.google.com/articles/CAIiECvj5X1hacDjSOEaklNYlM0qGQgEKhAIACoHCAow7pf_CjDdlfgCMKSi6gU?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Assam Minister Hints At \"Larger Solution\" Amid Mizoram Border Deadlock",
    "link": "https://news.google.com/articles/CAIiEK25arT5BBD8YgZ1sQg-LkUqGQgEKhAIACoHCAowj8n_CjDIrfkCMJWZ2AY?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "NMC notifies new norms for MBBS admissions, setting up of medical colleges; deletes 5-acre land req...",
    "link": "https://news.google.com/articles/CAIiECUkY1J10jpZlSLipuB_Oi0qFwgEKg4IACoGCAoww7k_MMevCDCKxq0G?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Seven Bengaluru hospitals put on notice for not setting up beds for BBMP-sponsored Covid-19 patients",
    "link": "https://news.google.com/articles/CBMirgFodHRwczovL3d3dy5uZXdpbmRpYW5leHByZXNzLmNvbS9jaXRpZXMvYmVuZ2FsdXJ1LzIwMjAvbm92LzAxL3NldmVuLWJlbmdhbHVydWhvc3BpdGFscy1wdXQtb24tbm90aWNlLWZvci1ub3Qtc2V0dGluZy11cC1iZWRzLWZvci1iYm1wLXNwb25zb3JlZC1jb3ZpZC0xOS1wYXRpZW50cy0yMjE3ODA1Lmh0bWzSAa0BaHR0cHM6Ly93d3cubmV3aW5kaWFuZXhwcmVzcy5jb20vY2l0aWVzL2JlbmdhbHVydS8yMDIwL25vdi8wMS9zZXZlbi1iZW5nYWx1cnVob3NwaXRhbHMtcHV0LW9uLW5vdGljZS1mb3Itbm90LXNldHRpbmctdXAtYmVkcy1mb3ItYmJtcC1zcG9uc29yZWQtY292aWQtMTktcGF0aWVudHMtMjIxNzgwNS5hbXA?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "People of West Bengal Paying Price for TMC Govt's Avoidable Confrontation with Centre: Governor",
    "link": "https://news.google.com/articles/CBMijAFodHRwczovL3d3dy5uZXdzMTguY29tL25ld3MvaW5kaWEvcGVvcGxlLW9mLXdlc3QtYmVuZ2FsLXBheWluZy1wcmljZS1mb3ItdG1jLWdvdnRzLWF2b2lkYWJsZS1jb25mcm9udGF0aW9uLXdpdGgtY2VudHJlLWdvdmVybm9yLTMwMzA0MDEuaHRtbNIBkAFodHRwczovL3d3dy5uZXdzMTguY29tL2FtcC9uZXdzL2luZGlhL3Blb3BsZS1vZi13ZXN0LWJlbmdhbC1wYXlpbmctcHJpY2UtZm9yLXRtYy1nb3Z0cy1hdm9pZGFibGUtY29uZnJvbnRhdGlvbi13aXRoLWNlbnRyZS1nb3Zlcm5vci0zMDMwNDAxLmh0bWw?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "PM Modi, Abhinandan posters come up in Pakistan leader’s constituency",
    "link": "https://news.google.com/articles/CAIiEJpVCAAucgcWx33THfaxVF4qGAgEKg8IACoHCAow3rvTBDD89X4w8ZXmBQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "After Leader's Return, Gorkha Group Says Mamata Banerjee Called For Talks",
    "link": "https://news.google.com/articles/CAIiEE1m8kXAwmzQlMxhZ26lBGEqGQgEKhAIACoHCAowj8n_CjDIrfkCMILSxQY?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Delhi public buses will run with full seating capacity, SOP to be issued in 1-2 days",
    "link": "https://news.google.com/articles/CAIiEIcmTWP2I0StliwWH0tgdpMqFwgEKg4IACoGCAowxLQ_MNevCDCF76cG?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Quit due to lack of reforms, run-ins with FM: Ex-finance secy Subhash Garg",
    "link": "https://news.google.com/articles/CAIiEL2UnKgalis2vYO1jxZ3nzUqGQgEKhAIACoHCAowzrL9CjDC7vQCMJCT1wU?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Delhi wakes up to chilly morning, temperature dips to 11.4°C",
    "link": "https://news.google.com/articles/CAIiEEtk92Dv2nmQptzxACOmxoEqFwgEKg4IACoGCAoww7k_MMevCDC0rdgG?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "NEET 2020 Andhra Pradesh list of candidates with 113 and more marks released, here’s direct link",
    "link": "https://news.google.com/articles/CAIiED0FGRYrEQFLVPf6gK3TW0wqFwgEKg4IACoGCAoww7k_MMevCDCKxq0G?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Adani Group takes over Mangaluru airport",
    "link": "https://news.google.com/articles/CBMia2h0dHBzOi8vd3d3LnRoZWhpbmR1LmNvbS9uZXdzL2NpdGllcy9NYW5nYWxvcmUvYWRhbmktZ3JvdXAtdGFrZXMtb3Zlci1tYW5nYWx1cnUtYWlycG9ydC9hcnRpY2xlMzI5OTQxNTMuZWNl0gFwaHR0cHM6Ly93d3cudGhlaGluZHUuY29tL25ld3MvY2l0aWVzL01hbmdhbG9yZS9hZGFuaS1ncm91cC10YWtlcy1vdmVyLW1hbmdhbHVydS1haXJwb3J0L2FydGljbGUzMjk5NDE1My5lY2UvYW1wLw?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "PAC Report Finds Kerala, Goa Best Governed States, UP Ranks Lowest",
    "link": "https://news.google.com/articles/CAIiEDg_i0ED6cWB8PRPrUg7YKwqGQgEKhAIACoHCAowwqP5CjDypeECMI6VwgU?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "CPI(M) open to Bengal alliance with Congress",
    "link": "https://news.google.com/articles/CAIiEAVTlw-GdL8rUzaF4u7Wjw8qFwgEKg4IACoGCAoww7k_MMevCDC8rdgG?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Pan India common phone number for Indane LPG refill bookings from today",
    "link": "https://news.google.com/articles/CAIiEOwGKdaNZufkM_PctXISxHsqFwgEKg4IACoGCAowxLQ_MNevCDDnvNMF?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Explained: What are the three farm Bills introduced by Rajasthan, what they seek to achieve",
    "link": "https://news.google.com/articles/CAIiELvBstPqp5U7aicqUEFFzUIqGAgEKg8IACoHCAow3rvTBDD89X4wwLbmBQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Rules relaxed, more guests allowed at weddings in Delhi",
    "link": "https://news.google.com/articles/CAIiEMxZ1Bby7KYsqFPXJzR0DaYqFwgEKg4IACoGCAoww7k_MMevCDC0rdgG?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "What Rajnath said & what US heard were different things",
    "link": "https://news.google.com/articles/CAIiEJXfsst8AzCpreZ0Vv9ZAN0qGQgEKhAIACoHCAowzrL9CjDC7vQCMK2y1gU?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Kerala beaches, parks and museums to be open for public from November 1",
    "link": "https://news.google.com/articles/CAIiEDlmdtdfhf2iYHuzNyBrFJIqGQgEKhAIACoHCAow7pf_CjDdlfgCMLTd6QU?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Rahul Gandhi at sister Priyanka Vadra’s cottage in Shimla",
    "link": "https://news.google.com/articles/CAIiEPlwkRMNKxzD67jE3Y-gdAEqGQgEKhAIACoHCAowyo-HCzD-tIUDMLfhlgY?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Unlock 6.0 guidelines: Which states have allowed more relaxations in November",
    "link": "https://news.google.com/articles/CAIiEK8XONXvYyUO0BotGfPtFkQqGAgEKg8IACoHCAow3rvTBDD89X4wwLbmBQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "\"100% Jobs Impossible Even If God Becomes Minister\": Goa Chief Minister",
    "link": "https://news.google.com/articles/CAIiEBMuMMZ9TE1cDHYv0hJzA4kqGQgEKhAIACoHCAowj8n_CjDIrfkCMPGi6AU?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "In last stretch, Dushyant hints at Cabinet berth for Dutt, Hooda recounts achievements",
    "link": "https://news.google.com/articles/CAIiECxsKkLRQTdrjlpEEnwGz74qGAgEKg8IACoHCAow3rvTBDD89X4w8ZXmBQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Chhattisgarh, Madhya Pradesh celebrate foundation day today; know history and significance",
    "link": "https://news.google.com/articles/CAIiEMLsPDCOkQ4g8srJjCbsHd0qGQgEKhAIACoHCAowib-NCzDawJ8DMLXSpwY?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "COVID-19 October 30 Highlights: Maharashtra reports 6,190 fresh cases",
    "link": "https://news.google.com/articles/CBMikQFodHRwczovL211bWJhaW1pcnJvci5pbmRpYXRpbWVzLmNvbS9jb3JvbmF2aXJ1cy9uZXdzL2NvdmlkLTE5LW9jdG9iZXItMzAtaGlnaGxpZ2h0cy1tYWhhcmFzaHRyYS1yZXBvcnRzLTYxOTAtZnJlc2gtY2FzZXMvYXJ0aWNsZXNob3cvNzg5NTc0MDcuY21z0gGVAWh0dHBzOi8vbXVtYmFpbWlycm9yLmluZGlhdGltZXMuY29tL2Nvcm9uYXZpcnVzL25ld3MvY292aWQtMTktb2N0b2Jlci0zMC1oaWdobGlnaHRzLW1haGFyYXNodHJhLXJlcG9ydHMtNjE5MC1mcmVzaC1jYXNlcy9hbXBfYXJ0aWNsZXNob3cvNzg5NTc0MDcuY21z?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Minister, Called \"Item\" By Kamal Nath, Banned From Campaigning For A Day",
    "link": "https://news.google.com/articles/CAIiEObwCRcC1XKw5FfwWyBpQNwqGQgEKhAIACoHCAowj8n_CjDIrfkCMILSxQY?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "After dropping steadily for over a month, active case count rises slightly in Pune",
    "link": "https://news.google.com/articles/CAIiEJRMqeehoEh9uHgxaLddvdgqGAgEKg8IACoHCAow3rvTBDD89X4w8YzmBQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "ICAI CA November admit card 2020 to be released today at icai.org, here’s how to download",
    "link": "https://news.google.com/articles/CAIiENibp8Ni2HyQht-xPgxXCp0qFwgEKg4IACoGCAoww7k_MMevCDCKxq0G?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Naseeruddin Shah, Prashant Bhushan Among 100 To Condemn France Attacks",
    "link": "https://news.google.com/articles/CAIiEEXJWRNoImqe1oZpYBK-mu0qGQgEKhAIACoHCAowj8n_CjDIrfkCMPGi6AU?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Piyush Goyal shares video of Bengaluru-Mysuru rail line passing ‘no water spill’ test",
    "link": "https://news.google.com/articles/CAIiEOVIB7ma-_VRW_yIYq3OyLwqGQgEKhAIACoHCAow7pf_CjDdlfgCMMOe6gU?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "COVID-19: Mumbai reports less than 1000 new cases on Saturday",
    "link": "https://news.google.com/articles/CBMiigFodHRwczovL211bWJhaW1pcnJvci5pbmRpYXRpbWVzLmNvbS9jb3JvbmF2aXJ1cy9uZXdzL2NvdmlkLTE5LW11bWJhaS1yZXBvcnRzLWxlc3MtdGhhbi0xMDAwLW5ldy1jYXNlcy1vbi1zYXR1cmRheS9hcnRpY2xlc2hvdy83ODk3MjU4OS5jbXPSAY4BaHR0cHM6Ly9tdW1iYWltaXJyb3IuaW5kaWF0aW1lcy5jb20vY29yb25hdmlydXMvbmV3cy9jb3ZpZC0xOS1tdW1iYWktcmVwb3J0cy1sZXNzLXRoYW4tMTAwMC1uZXctY2FzZXMtb24tc2F0dXJkYXkvYW1wX2FydGljbGVzaG93Lzc4OTcyNTg5LmNtcw?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Capt Amarinder Singh rolls out SC scheme, 3 lakh pupils to benefit",
    "link": "https://news.google.com/articles/CAIiEACZX12aQ9yj2mmigPABUg8qGQgEKhAIACoHCAowyo-HCzD-tIUDMLfhlgY?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "BJP tries to curb rising infighting in its Bengal unit",
    "link": "https://news.google.com/articles/CBMicmh0dHBzOi8vd3d3LmRlY2NhbmNocm9uaWNsZS5jb20vbmF0aW9uL3BvbGl0aWNzLzMxMTAyMC9ianAtdHJpZXMtdG8tY3VyYi1yaXNpbmctaW5maWdodGluZy1pbi1pdHMtYmVuZ2FsLXVuaXQuaHRtbNIBdmh0dHBzOi8vd3d3LmRlY2NhbmNocm9uaWNsZS5jb20vYW1wL25hdGlvbi9wb2xpdGljcy8zMTEwMjAvYmpwLXRyaWVzLXRvLWN1cmItcmlzaW5nLWluZmlnaHRpbmctaW4taXRzLWJlbmdhbC11bml0Lmh0bWw?hl=en-IN&gl=IN&ceid=IN%3Aen"
  },
  {
    "head": "Delhi’s water supply hit, DJB asks UP to expedite work on canal",
    "link": "https://news.google.com/articles/CAIiEEJG8C8RgqzTZhTgK1FQW1QqGAgEKg8IACoHCAow3rvTBDD89X4w8YzmBQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
  }
]
```

## **Star the Repo in case you liked it :)**
### © [Dhanush N](https://github.com/RorYin)
   
   
   
