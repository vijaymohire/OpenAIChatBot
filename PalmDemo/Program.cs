using Google.Ai.Generativelanguage.V1Beta2;
using Google.Api.Gax.Grpc;
using Google.Apis.Auth.OAuth2;

const string apiKey = "MY_KEY";
var callSettings = CallSettings.FromHeader("x-goog-api-key", apiKey);

var clientBuilder = new DiscussServiceClientBuilder
{
    GoogleCredential = GoogleCredential.FromAccessToken(null),
    Settings = new DiscussServiceSettings
    {
        CallSettings = callSettings
    }
};
var client = clientBuilder.Build();

while (true)
{
    Console.Write("Message (type 'exit' to leave): ");
    var message = Console.ReadLine();

    if (string.IsNullOrWhiteSpace(message) || message.Equals("exit", StringComparison.InvariantCultureIgnoreCase))
    {
        break;
    }

    var prompt = new MessagePrompt();
    prompt.Messages.Add(new Message
    {
        Content = message
    });

    var request = new GenerateMessageRequest
    {
        ModelAsModelName = ModelName.FromModel("chat-bison-001"),
        Prompt = prompt,
        Temperature = 0.5F,
        CandidateCount = 1
    };
    var response = await client.GenerateMessageAsync(request);
    Console.WriteLine(response.Candidates[0].Content);
}