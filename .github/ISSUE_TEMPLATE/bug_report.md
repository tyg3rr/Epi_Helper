name: Bug report
about: Create a report to help us improve
title: ''
labels: [bug, triage]
assignees: ''
  - type: input
    id: contact
    attributes:
    label: Contact Details
    description: How can we get in touch with you if we need more info?
    placeholder: ex. email@example.com
    validations:
      required: false
  - type: textarea
    id: what-happened
    attributes:
    label: What happened?
    description: Also tell us, what did you expect to happen?
    placeholder: Tell us what you see!
    value: "A bug happened!"
    validations:
      required: true
  - type: textarea
    id: additional-info
    attributes:
    label: Additional Information
    description: Anything else you'd like to add?
    placeholder: I like dogs
    value: "Extra Comments"
    validations:
      required: false
  - type: textarea
    id: logs
    attributes:
    label: Relevant log output
    description: Please copy and paste any relevant log output. This will be automatically formatted into code, so no need for backticks.
    render: shell
# Enable after setting up a C.O.C.
#   - type: checkboxes
#     id: terms
#     attributes:
#       label: Code of Conduct
#       description: By submitting this issue, you agree to follow our [Code of Conduct](https://example.com)
#       options:
#         - label: I agree to follow this project's Code of Conduct
#           required: true


**Anything else you would like to add:**

<!-- Note: Miscellaneous information that will assist in solving the issue. -->

**Additional Information:**

<!-- Note: Anything to give further context to the bug report. -->
