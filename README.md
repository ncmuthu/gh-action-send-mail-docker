# gh-action-send-mail-docker

# Usage

<!-- start usage -->
```yaml
      - name: Call Send Email Action
        uses: ncmuthu/gh-action-send-mail-docker/send-email-action@main
        with:
          to_email: ${{ secrets.TO_EMAIL }}
          from_email: ${{ secrets.FROM_EMAIL }}
          smtp_server: ${{ secrets.SMTP_SERVER }}
          smtp_port: ${{ secrets.SMTP_PORT }}
          smtp_username: ${{ secrets.SMTP_USERNAME }}
          smtp_password: ${{ secrets.SMTP_PASSWORD }}
          subject: "Test email using gh action"
          body: "Test email from gh"
```
<!-- end usage -->

# Test
