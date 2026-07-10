FROM golang:1.25

ENV PACKAGE_TO_SCAN=$PACKAGE_TO_SCAN

WORKDIR /github/workspace

RUN go install go.uber.org/nilaway/cmd/nilaway@latest

# The checked-out repository at /github/workspace is owned by the runner's
# host user, not this container's user, which newer git versions treat as
# "dubious ownership" and refuse to touch. That breaks Go's VCS stamping
# (`go build`/`go vet` fail with "error obtaining VCS status: exit status
# 128"), which cascades into nilaway skipping every analyzer. Trust any
# workspace mounted into the container.
RUN git config --global --add safe.directory '*'

ENTRYPOINT ["sh", "-c", "nilaway $PACKAGE_TO_SCAN"]
