// using Twilio SendGrid's v3 Node.js Library
// https://github.com/sendgrid/sendgrid-nodejs

const sgMail = require("@sendgrid/mail");
console.log("the value of process" + process.env.SENDGRID_API_KEY);

sgMail.setApiKey(process.env.SENDGRID_API_KEY);

const msg = {
	to: "kautilyasave@gmail.com", // Change to your recipient
	from: "L@Kautilya.com", // Change to your verified sender
	subject: "Hello SensehacK!",
	text:
		"You need to upgrade your email client to rich html parser based viewer.",
	html:
		"<strong>That's more like it! Spark by Readdle is my recommendation for great email client.</strong>",
};
sgMail
	.send(msg)
	.then(() => {
		console.log("Email sent");
	})
	.catch((error) => {
		console.error(error);
	});
