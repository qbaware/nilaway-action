FROM golang:1.21

ENV PACKAGE_TO_SCAN=$PACKAGE_TO_SCAN

WORKDIR /github/workspace

RUN go install go.uber.org/nilaway/cmd/nilaway@latest

ENTRYPOINT nilaway ${PACKAGE_TO_SCAN}
