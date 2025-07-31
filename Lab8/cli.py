import subprocess
import click
import os

@click.group()
def cli():
    """Simple CLI for managing Docker services (MinIO, Postfix, Redis)"""
    pass

@cli.command()
def start():
    """Start all Docker services"""
    subprocess.run(["docker-compose", "up", "-d"])

@cli.command()
def stop():
    """Stop all Docker services"""
    subprocess.run(["docker-compose", "down"])

@cli.command()
@click.argument("service")
def show_logs(service):
    """Show logs of a service (e.g., minio, redis, postfix)"""
    subprocess.run(["docker", "logs", service])

@cli.command()
@click.argument("key")
@click.argument("value")
def redis_set(key, value):
    """Set a Redis key-value pair"""
    subprocess.run([
        "docker", "exec", "redis", 
        "redis-cli", "set", key, value
    ])

@cli.command()
@click.argument("key")
def redis_get(key):
    """Get a Redis key"""
    subprocess.run([
        "docker", "exec", "redis", 
        "redis-cli", "get", key
    ])

@cli.command()
@click.argument("to_email")
@click.argument("subject")
@click.argument("body")
def send_email(to_email, subject, body):
    """Send test email using Postfix"""
    cmd = f'echo "Subject: {subject}\n\n{body}" | sendmail {to_email}'
    subprocess.run([
        "docker", "exec", "-i", "postfix", "sh", "-c", cmd
    ])
    print(f"Email sent to {to_email}")

@cli.command()
@click.argument("bucket")
@click.argument("file_path")
def upload_minio(bucket, file_path):
    """Upload file to MinIO bucket"""
    subprocess.run(["mc", "alias", "set", "local", "http://localhost:9000", "minioadmin", "minioadmin"])
    subprocess.run(["mc", "mb", f"local/{bucket}"], stderr=subprocess.DEVNULL)  # skip error if bucket exists
    subprocess.run(["mc", "cp", file_path, f"local/{bucket}/"])
    print(f"Uploaded {file_path} to bucket {bucket}")

if __name__ == "__main__":
    cli()
