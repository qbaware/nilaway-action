FROM golang:1.22

ENV PACKAGE_TO_SCAN=$PACKAGE_TO_SCAN

WORKDIR /github/workspace

RUN go install go.uber.org/nilaway/cmd/nilaway@latest

ENTRYPOINT ["sh", "-c", "nilaway $PACKAGE_TO_SCAN"]
