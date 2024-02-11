import os
import docker


def test_healthy_package(client, image):
    print("Testing healthy package...")

    container = client.containers.run(
        image,
        volumes={os.getcwd(): {"bind": "/test", "mode": "rw"}},
        working_dir="/test/healthypkg/",
        entrypoint="nilaway ./...",
        detach=True,
    )

    exit_code = container.wait()
    logs = container.logs(stdout=True, stderr=True).decode("utf-8")
    print(exit_code, "\n", logs)

    container.stop()
    container.remove()

    assert exit_code["StatusCode"] == 0
    assert "Potential nil panic detected" not in logs


def test_unhealthy_package(client, image):
    print("Testing unhealthy package...")

    container = client.containers.run(
        image,
        volumes={os.getcwd(): {"bind": "/test", "mode": "rw"}},
        working_dir="/test/unhealthypkg/",
        entrypoint="nilaway ./...",
        detach=True,
    )

    exit_code = container.wait()
    logs = container.logs(stdout=True, stderr=True).decode("utf-8")
    print(exit_code, "\n", logs)

    container.stop()
    container.remove()

    assert exit_code["StatusCode"] != 0
    assert "Potential nil panic detected" in logs


def main():
    client = docker.from_env()
    image, _ = client.images.build(path="../", tag="nilaway-action-test-image", rm=True)

    test_healthy_package(client, image)
    test_unhealthy_package(client, image)

    print("All tests passed!")

    client.images.remove(image.id)


if __name__ == "__main__":
    main()
