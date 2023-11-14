import { createApp } from 'vue';
import App1 from './App1.vue';
import { createRouter, createWebHistory } from 'vue-router';
import Routes from './routes';

const app1 = createApp(App1);
const router = createRouter({
  history: createWebHistory(),
  routes: Routes,
});
app1.use(router);

app1.mount('#app1');




const request = require('request');

app.post('/api/v1/index', (req, res) => {
  const recaptchaResponse = req.body['g-recaptcha-response'];
  const secretKey = '6LcEiOooAAAAAEiFfdK2u69RgvX7Y7OJJSHjv4j3';

  // Verify the reCAPTCHA token
  request.post(
    {
      url: 'https://www.google.com/recaptcha/api/siteverify',
      form: {
        secret: secretKey,
        response: recaptchaResponse,
      },
    },
    (error, response, body) => {
      body = JSON.parse(body);
      if (body.success !== undefined && !body.success) {
        // CAPTCHA verification failed
        res.status(403).send('CAPTCHA verification failed.');
      } else {
        // CAPTCHA verification passed; process the login logic here
        // ...
      }
    }
  );
});
