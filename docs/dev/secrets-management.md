# Secrets Management

This guide explains how to manage secrets and environment variables in the PyPlate FastAPI project.

## Local Development

For local development, we use `.env` files to manage environment variables. This approach keeps sensitive information like API keys and database credentials out of the source code.

### Setting Up Your Local Environment

1. Copy the example environment file to create your own:

   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file with your own values:

   ```ini
   # Authentication
   SECRET_KEY=your-very-secret-key-here
   
   # Database settings
   POSTGRES_PASSWORD=your-database-password
   ```

3. The application will automatically load these variables when it starts.

### Important Notes

- **NEVER** commit your `.env` file to version control
- The `.env.example` file serves as documentation for available variables
- For development, SQLite is used by default (no additional setup required)
- For production or testing with PostgreSQL, set the appropriate PostgreSQL environment variables

## GitHub Actions Secrets

For CI/CD workflows in GitHub Actions, we use GitHub's built-in secrets management.

### Adding Secrets to GitHub Repository

1. Navigate to your GitHub repository
2. Go to **Settings > Secrets and variables > Actions**
3. Click **New repository secret**
4. Add each required secret:
   - `SECRET_KEY`: The secret key for JWT token signing
   - `POSTGRES_PASSWORD`: Password for the test/CI database
   - `DOCKER_REGISTRY_TOKEN`: Token for pushing Docker images (if applicable)

### Using Secrets in GitHub Workflows

Secrets are available in GitHub workflow files as `${{ secrets.SECRET_NAME }}`:

```yaml
jobs:
  test:
    steps:
      - name: Run tests
        env:
          SECRET_KEY: ${{ secrets.SECRET_KEY }}
          POSTGRES_PASSWORD: ${{ secrets.POSTGRES_PASSWORD }}
        run: make test
```

## Production Secrets Management

For production deployment, consider these secure approaches:

### Docker/Docker Compose

Use environment variables or Docker secrets:

```yaml
# docker-compose.yml
services:
  api:
    environment:
      - SECRET_KEY=${SECRET_KEY}
    secrets:
      - db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

### Cloud Providers

Most cloud providers offer secrets management services:

- **AWS**: AWS Secrets Manager or Parameter Store
- **Azure**: Key Vault
- **Google Cloud**: Secret Manager

## Best Practices

1. **Rotation**: Regularly rotate sensitive credentials
2. **Least Privilege**: Use credentials with minimal required permissions
3. **Separation**: Use different credentials for development, testing, and production
4. **Auditing**: Maintain logs of who accesses secrets and when (in production)
5. **No Hardcoding**: Never hardcode secrets in source code or config files
6. **No Logging**: Ensure secrets aren't included in application logs