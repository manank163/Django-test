function validateform()
			{
 
				var x=document.forms["myform"]["name"].value;
				if (x==null || x=="")
				{
					alert("First name must be filled out");
					document.myform.name.focus();
					return false;
				}
				var y=document.forms["myform"]["email"].value;
				if (y==null || y=="")
				{
					alert("Please provide with your email");
					document.myform.email.focus();
					
					return false;
				}
				var passwordid=document.forms["myform"]["pwd"].value;
				var pass_length=passwordid.length;
				if(pass_length<=7)
				{
					alert("please provide with a password greater than 7 digits");
					document.myform.pwd.focus();
					return false;
				}
				var conf_pass=document.forms["myform"]["confpwd"].value;
				if(conf_pass!=passwordid)
				{
					alert("Please confirm your password correctly");
					return false;
				}
				var mobile_nu=document.forms["myform"]["mob"].value;
				if(mobile_nu.length!=10)
				{
					alert("Enter a valid mobile number");
					document.myform.mob.focus();
					return false;
				}
				return true;
			}
			
			