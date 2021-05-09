using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;

public class WebRequesterGPT2 : MonoBehaviour
{
    InputField InputField; // Seed for the model request
    InputField Leng;       // Character length of the token to receive from the request
    Text Response;         // Text field to parse the response from the model into
    Dropdown Drop;         // Dropdown UI element for choosing the theme
    string received;       
    // Start is called before the first frame update
    void Start()
    {
        InputField = GameObject.Find("InputField").GetComponent<InputField>();
        Leng = GameObject.Find("Leng").GetComponent<InputField>();
        Response = GameObject.Find("Response Text").GetComponent<Text>();
        Drop = GameObject.Find("Dropdown").GetComponent<Dropdown>();
    }

    IEnumerator GetRequest(string uri)
    {
        using (UnityWebRequest webRequest = UnityWebRequest.Get(uri))
        {
            // Request and wait for the desired page.
            yield return webRequest.SendWebRequest();

            string[] pages = uri.Split('/');
            int page = pages.Length - 1;

            if (webRequest.isNetworkError)
            {
                Debug.Log(pages[page] + ": Error: " + webRequest.error);
                received = "Error: " + webRequest.error;
                Response.text = received;
            }
            else
            {
                Debug.Log(pages[page] + ":\nReceived: " + webRequest.downloadHandler.text);
                received = webRequest.downloadHandler.text;
                Response.text = received;
            }
        }
    }

    // http://<IPOFSERVERHOSTINGWEBAPI>/api/v1/speech?speech=
    public void OnPress()
    {
        string preamble = "http://<IPOFSERVERHOSTINGWEBAPI>/api/v1/speech?speech=";
        string requestToken = InputField.text.ToString();
        if (requestToken == null) requestToken = "<DEFAULT MODEL SEED>";
        string leng = Leng.text.ToString();
        if (leng == null) leng = "100";
        string lengToken = "&leng=" + leng;
        string model = Drop.options[Drop.value].text.ToString();
        string modelToken = "&style=" + model;
        string request = preamble + requestToken + modelToken;
        StartCoroutine(GetRequest(request));
        Response.text = received;
    }
}
